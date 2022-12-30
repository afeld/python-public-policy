import dataclasses
from jinja2 import Environment
from nbconvert.preprocessors import Preprocessor
from nbformat import NotebookNode
from traitlets import Unicode


@dataclasses.dataclass
class SchoolText:
    """Class to ensure each school has matching keys"""

    school_name: str
    school_slug: str
    course_name: str
    lms_name: str
    lms_url: str
    discussions_url: str
    lms_notification_settings_url: str
    words: list[str]


COURSE_HOSTNAME = "python-public-policy.afeld.me"
# the keys are the slugs
SCHOOL_TEXT = {
    "columbia": SchoolText(
        school_name="Columbia University",
        school_slug="columbia",
        course_name="Python for Public Policy",
        lms_name="CourseWorks",
        lms_url="https://courseworks2.columbia.edu/courses/171519",
        discussions_url="https://courseworks2.columbia.edu/courses/171519/discussion_topics",
        lms_notification_settings_url="https://courseworks2.columbia.edu/profile/communication",
        words=[
            "columbia",
            "courseworks",
            "python for public policy",
            "sipa",
        ],
    ),
    "nyu": SchoolText(
        school_name="NYU Wagner",
        school_slug="nyu",
        course_name="Python Coding for Public Policy",
        lms_name="Brightspace",
        lms_url="https://brightspace.nyu.edu/d2l/home/206261",
        discussions_url="https://brightspace.nyu.edu/d2l/le/206261/discussions/List",
        lms_notification_settings_url="https://brightspace.nyu.edu/d2l/lms/discussions/admin/subscriptions.d2l?ou=156784",
        words=[
            "brightspace",
            # "conversation",  # Brightspace term, TODO
            "nyu",
            "padm",
            "python coding for public policy",  # Columbia version doesn't include "Coding"
            "wagner",
        ],
    ),
}
EXEMPT = [
    "hannahkates/nyu-python-public-policy",
    "rcnyu.org",  # TODO
]

env = Environment()


def render_template(source: str, school_slug: str):
    template = env.from_string(source)

    school_text = SCHOOL_TEXT[school_slug]
    local_vars = dataclasses.asdict(school_text)

    return template.render(**local_vars)


def check_line(line: str, line_num: int, this_school: SchoolText):
    other_schools = [
        other_school
        for other_school in SCHOOL_TEXT.values()
        if other_school.school_slug != this_school.school_slug
    ]
    for other_school in other_schools:
        for word in other_school.words:
            for exemption in EXEMPT:
                if exemption in line.lower():
                    return

            msg = f'"{word}" found, line {line_num}:\n\n{line}'
            assert word not in line.lower(), msg

    # site check
    if COURSE_HOSTNAME in line:
        # (imperfectly) assure it's linking to the right version
        assert (
            f"{COURSE_HOSTNAME}/en/{this_school.school_slug}" in line
        ), f"Not properly linking to course site, line {line_num}:\n\n{line}"


def confirm_other_schools_not_included(source: str, school_slug: str):
    school_text = SCHOOL_TEXT[school_slug]
    for i, line in enumerate(source.splitlines()):
        line_num = i + 1
        check_line(line, line_num, school_text)


def render_cell(cell: NotebookNode, school_slug: str):
    cell.source = render_template(cell.source, school_slug)
    confirm_other_schools_not_included(cell.source, school_slug)
    return cell


# https://nbconvert.readthedocs.io/en/latest/nbconvert_library.html#Custom-Preprocessors
class SchoolTemplate(Preprocessor):
    school_slug = Unicode().tag(config=True)

    def preprocess_cell(self, cell: NotebookNode, resources, cell_index):
        if not self.school_slug:
            raise RuntimeError(f"{type(self).__name__}.school_slug must be set")

        cell = render_cell(cell, self.school_slug)
        return cell, resources
