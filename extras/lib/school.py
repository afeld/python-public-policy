import dataclasses
from jinja2 import Environment
from nbconvert.preprocessors import Preprocessor
from nbformat import NotebookNode
from traitlets import Unicode


@dataclasses.dataclass
class SchoolText:
    """Class to ensure each school has matching keys"""

    school_name: str
    course_name: str
    lms_name: str
    lms_url: str
    discussions_url: str
    lms_notification_settings_url: str


SCHOOL_TEXT = {
    "columbia": SchoolText(
        school_name="Columbia University",
        course_name="Python for Public Policy",
        lms_name="CourseWorks",
        lms_url="https://courseworks2.columbia.edu/courses/171519",
        discussions_url="https://courseworks2.columbia.edu/courses/171519/discussion_topics",
        lms_notification_settings_url="https://courseworks2.columbia.edu/profile/communication",
    ),
    "nyu": SchoolText(
        school_name="NYU Wagner",
        course_name="Python Coding for Public Policy",
        lms_name="Brightspace",
        lms_url="https://brightspace.nyu.edu/d2l/home/206261",
        discussions_url="https://brightspace.nyu.edu/d2l/le/206261/discussions/List",
        lms_notification_settings_url="https://brightspace.nyu.edu/d2l/lms/discussions/admin/subscriptions.d2l?ou=156784",
    ),
}
env = Environment()


def render_template(source: str, school_slug: str):
    template = env.from_string(source)

    local_vars = dataclasses.asdict(SCHOOL_TEXT[school_slug])
    local_vars["school_slug"] = school_slug

    return template.render(**local_vars)


def render_cell(cell: NotebookNode, school_slug: str):
    cell.source = render_template(cell.source, school_slug)
    return cell


# https://nbconvert.readthedocs.io/en/latest/nbconvert_library.html#Custom-Preprocessors
class SchoolTemplate(Preprocessor):
    school_slug = Unicode().tag(config=True)

    def preprocess_cell(self, cell: NotebookNode, resources, cell_index):
        if not self.school_slug:
            raise RuntimeError(f"{type(self).__name__}.school_slug must be set")

        cell = render_cell(cell, self.school_slug)
        return cell, resources
