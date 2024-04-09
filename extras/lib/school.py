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
    discussions_url: str
    survey_url: str
    name_tool_url: str
    lms_profile_pic_url: str
    lms_notification_settings_url: str
    lms_grading_docs: str
    lms_reorder_docs: str
    coding_env_name: str
    coding_env_url: str
    coding_env_kernel_name: str
    assistant_name: str
    assistant_responsibilities: str
    wait_list: str
    auditing: str
    r_credit: str
    assignment_cutoff_name: str
    python_for_mbas: str
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
        lms_url="https://courseworks2.columbia.edu/courses/187089",
        discussions_url="https://courseworks2.columbia.edu/courses/187089/external_tools/37606?display=borderless",
        survey_url="https://courseworks2.columbia.edu/courses/187089/external_tools/37606?display=borderless",
        name_tool_url="https://courseworks2.columbia.edu/courses/187089/external_tools/39295",
        lms_profile_pic_url="https://courseworks2.columbia.edu/profile",
        lms_notification_settings_url="https://edstem.org/us/settings/notifications",
        lms_grading_docs="https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-use-SpeedGrader/ta-p/757",
        lms_reorder_docs="https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-move-or-reorder-an-assignment/ta-p/1289",
        coding_env_name="Google Colab",
        coding_env_url="https://colab.research.google.com",
        coding_env_kernel_name="runtime",
        assistant_name="Reader",
        assistant_responsibilities="https://docs.google.com/document/d/1NiS1uPM_0OB7dXHP1D90P-XikXj6gwWRUsf0V_dEoUI/edit#heading=h.7f7yn4ehwnkz",
        wait_list="https://www.registrar.columbia.edu/content/wait-lists-ssol",
        auditing="https://www.sipa.columbia.edu/students/student-affairs/academic-advising-faq",
        r_credit="https://www.registrar.columbia.edu/content/grade-options#auditing",
        assignment_cutoff_name="`Until` date",
        python_for_mbas="https://clio.columbia.edu/catalog/15536430",
        final_project_proposal="https://edstem.org",
        words=[
            "canvaslms",
            "colab",
            "columbia",
            "courseworks",
            "daqa",
            "leigh",
            "python for public policy",
            "reader",
            "sebastian",
            "sipa",
            "speedgrader",
        ],
    ),
    SchoolText(
        id="nyu",
        school_name="NYU Wagner",
        school_slug="nyu",
        color="#57058b",
        course_name="Python Coding for Public Policy",
        lms_name="Brightspace",
        lms_url="https://brightspace.nyu.edu/d2l/home/366164",
        discussions_url="https://brightspace.nyu.edu/d2l/le/lessons/366164/topics/9996174",
        survey_url="https://docs.google.com/forms/d/e/1FAIpQLSdkzIFobWpqWZpfjioN4JiRD3pPR2ADJJkuRmVfUnI7w2vlxg/viewform?usp=sf_link",
        name_tool_url="https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/forms-policies-procedures/pronouns-and-name-pronunciation.html#S1",
        lms_profile_pic_url="https://community.d2l.com/brightspace/kb/articles/18108-change-personal-settings-in-brightspace",
        lms_notification_settings_url="https://brightspace.nyu.edu/d2l/lms/discussions/admin/subscriptions.d2l?ou=366164",
        lms_grading_docs="https://community.d2l.com/brightspace/kb/articles/3529-evaluate-assignments-using-the-assignments-tool",
        lms_reorder_docs="https://community.d2l.com/brightspace/kb/articles/3405-reorder-edit-and-delete-assignments-and-categories",
        coding_env_name="JupyterHub",
        coding_env_url="https://padm-4506-spring.rcnyu.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fafeld%2Fpython-public-policy&urlpath=tree%2Fpython-public-policy%2F&branch=nyu",
        coding_env_kernel_name="kernel",
        assistant_name="grader",
        assistant_responsibilities="https://docs.google.com/document/d/1dX2MDc5Fhby8GyeKLF4rrI0RZrJAmF1LHGV2SdFIkAE/edit#heading=h.7f7yn4ehwnkz",
        wait_list="https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/albert-help/training/students/registration/waitlists.html",
        auditing="https://wagner.nyu.edu/portal/students/academics/registration/auditing",
        r_credit="https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/transcripts-certifications-grades/grades.html",
        assignment_cutoff_name="`End Date`",
        python_for_mbas="https://bobcat.library.nyu.edu/permalink/f/ci13eu/nyu_aleph008975996",
        final_project_proposal="https://edstem.org/us/courses/56920/discussion/4727810",
        words=[
            "amisa",
            "bonus",
            "brightspace",
            "conda",
            # "conversation",  # Brightspace term, TODO
            "grader",
            "jupyterhub",
            "nyu",
            "padm",
            "peermark",
            "python coding for public policy",  # Columbia version doesn't include "Coding"
            "regrad",
            "re-grad",
            "re-submi",
            "resubmi",
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
    "dictreader",
    "for row in reader",
    "hannahkates/nyu-python-public-policy",
    "jupyterhub_url",
    "name: install conda packages",  # CI
    "nbgrader",
    "nyu's quantitative analysis guide",
    "upload the notebook to [google colab]",
    "upload the python file to google colab",
    "https://community.canvaslms.com/t5/canvas-basics-guide/what-are-grading-schemes/ta-p/41",
    "python coding for public policy assignments",
    "secondary",  # matches "conda"
    "set up the reader",
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
