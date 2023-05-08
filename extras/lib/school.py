import dataclasses
from jinja2 import Environment
from nbconvert.preprocessors import Preprocessor
from nbformat import NotebookNode
from traitlets import Unicode
from typing import List


@dataclasses.dataclass
class SchoolText:
    """Class to ensure each school has the same configuration structure"""

    id: str
    school_name: str
    school_slug: str
    color: str
    course_name: str
    lms_name: str
    lms_url: str
    lms_anonymous_docs: str
    discussions_url: str
    survey_url: str
    lms_notification_settings_url: str
    coding_env_name: str
    coding_env_url: str
    assistant_name: str
    assistant_responsibilities: str
    words: List[str]


COURSE_HOSTNAME = "python-public-policy.afeld.me"
SCHOOLS = [
    SchoolText(
        id="columbia",
        school_name="Columbia University",
        school_slug="columbia",
        color="#201D5D",
        course_name="Python for Public Policy",
        lms_name="CourseWorks",
        lms_url="https://courseworks2.columbia.edu/courses/171519",
        lms_anonymous_docs="https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-add-an-assignment-that-includes-anonymous-grading/ta-p/769",
        discussions_url="https://courseworks2.columbia.edu/courses/171519/external_tools/37606?display=borderless",
        survey_url="https://courseworks2.columbia.edu/courses/171519/external_tools/37606?display=borderless",
        lms_notification_settings_url="https://edstem.org/us/settings/notifications",
        coding_env_name="Google Colab",
        coding_env_url="https://colab.research.google.com",
        assistant_name="Reader",
        assistant_responsibilities="https://docs.google.com/document/d/1NiS1uPM_0OB7dXHP1D90P-XikXj6gwWRUsf0V_dEoUI/edit#heading=h.7f7yn4ehwnkz",
        words=[
            "canvaslms",
            "colab",
            "columbia",
            "courseworks",
            "ed discussion",
            "edstem",
            "kellyann",
            "mostafa",
            "reader",
            "python for public policy",
            "sipa",
            "speedgrader",
            "wait list",
        ],
    ),
    SchoolText(
        id="nyu",
        school_name="NYU Wagner",
        school_slug="nyu",
        color="#57058b",
        course_name="Python Coding for Public Policy",
        lms_name="Brightspace",
        lms_url="https://brightspace.nyu.edu/d2l/home/278596",
        lms_anonymous_docs="https://documentation.brightspace.com/EN/le/assignments/instructor/about_anonymous_marking.htm",
        discussions_url="https://brightspace.nyu.edu/d2l/le/278596/discussions/List",
        survey_url="https://brightspace.nyu.edu/d2l/lms/survey/admin/stats/survey_view_overall.d2l?ou=278596&si=297833",
        lms_notification_settings_url="https://brightspace.nyu.edu/d2l/lms/discussions/admin/subscriptions.d2l?ou=278596",
        coding_env_name="JupyterHub",
        coding_env_url="https://padmgp-4506.rcnyu.org/user-redirect/notebooks/class_materials/",
        assistant_name="grader",
        assistant_responsibilities="https://docs.google.com/document/d/1dX2MDc5Fhby8GyeKLF4rrI0RZrJAmF1LHGV2SdFIkAE/edit#heading=h.7f7yn4ehwnkz",
        words=[
            "amisa",
            "brightspace",
            "conda",
            # "conversation",  # Brightspace term, TODO
            "grader",
            "jupyterhub",
            "nyu",
            "padm",
            "peermark",
            "pio.renderers.default",  # boilerplate for allowing PDF export
            "python coding for public policy",  # Columbia version doesn't include "Coding"
            "turnitin",
            "wagner",
        ],
    ),
]
SCHOOL_TEXT = {school.id: school for school in SCHOOLS}
# should all be lowercase
EXEMPT = [
    "- [google colab](https://colab.research.google.com/)",
    "anaconda",
    "built around it",  # referring to Colab
    "columbia's graduate school of architecture",  # bio
    "conda activate",
    "create the environment",
    "hannahkates/nyu-python-public-policy",
    "jupyterhub_url",
    "nbgrader",
    "nyu's quantitative analysis guide",
    "upload the notebook to [google colab]",
    "python coding for public policy assignments",
    "secondary",  # matches "conda"
    "speedgrader",  # matches "grader"
    "these instructions won't work in colab",
    "walk the reader",
]

env = Environment()


def render_template(source: str, school_id: str):
    template = env.from_string(source)

    school_text = SCHOOL_TEXT[school_id]
    local_vars = dataclasses.asdict(school_text)

    return template.render(**local_vars)


def check_line(line: str, line_num: int, this_school: SchoolText):
    lower_line = line.lower()
    other_schools = [other_school for other_school in SCHOOLS if other_school.id != this_school.id]

    for other_school in other_schools:
        for word in other_school.words:
            for exemption in EXEMPT:
                if exemption in lower_line:
                    return

            msg = f'"{word}" found, line {line_num}:\n\n{line}\n'
            assert word not in lower_line, msg

    # site check
    if COURSE_HOSTNAME in line:
        # (imperfectly) assure it's linking to the right version
        assert (
            f"{COURSE_HOSTNAME}/en/{this_school.school_slug}" in line
        ), f"Not properly linking to course site, line {line_num}:\n\n{line}\n"


def confirm_other_schools_not_included(source: str, school_id: str):
    school_text = SCHOOL_TEXT[school_id]
    for i, line in enumerate(source.splitlines()):
        line_num = i + 1
        check_line(line, line_num, school_text)


def render_cell(cell: NotebookNode, school_id: str):
    cell.source = render_template(cell.source, school_id)
    confirm_other_schools_not_included(cell.source, school_id)
    return cell


# https://nbconvert.readthedocs.io/en/latest/nbconvert_library.html#Custom-Preprocessors
class SchoolTemplate(Preprocessor):
    school_id = Unicode().tag(config=True)

    def preprocess(self, nb, resources):
        if self.school_id == "columbia":
            # use default kernel for Colab
            nb.metadata.kernelspec = {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            }

        return super().preprocess(nb, resources)

    def preprocess_cell(self, cell: NotebookNode, resources, cell_index):
        if not self.school_id:
            raise RuntimeError(f"{type(self).__name__}.school_id must be set")

        cell = render_cell(cell, self.school_id)
        return cell, resources
