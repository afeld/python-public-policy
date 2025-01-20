import dataclasses
from typing import List


@dataclasses.dataclass
class SchoolText:
    """Class to ensure each school has the same configuration structure"""

    id: str
    school_name: str
    school_slug: str
    color: str
    course_name: str
    term: str
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
    coding_env_origin: str
    coding_env_kernel_name: str
    assistant_name: str
    assistant_responsibilities: str
    wait_list: str
    registration: str
    cross_registration: str
    auditing: str
    r_credit: str
    assignment_cutoff_name: str
    python_for_mbas: str
    statista_url: str
    final_project_proposal: str
    attendance_url: str
    words: List[str]


SCHOOLS = [
    SchoolText(
        id="columbia",
        school_name="Columbia University",
        school_slug="columbia",
        color="#201D5D",
        course_name="Python for Public Policy",
        term="Spring 2025",
        lms_name="CourseWorks",
        lms_url="https://courseworks2.columbia.edu/courses/210776",
        discussions_url="https://courseworks2.columbia.edu/courses/210776/external_tools/37606?display=borderless",
        survey_url="https://docs.google.com/forms/d/e/1FAIpQLSeexomJkVX-9WTMXTYfRYWg3UC3n0_gDVe-qGDDt78aTbBodw/viewform?usp=header",
        name_tool_url="https://courseworks2.columbia.edu/courses/210776/external_tools/62951",
        lms_profile_pic_url="https://courseworks2.columbia.edu/profile",
        lms_notification_settings_url="https://edstem.org/us/settings/notifications",
        lms_grading_docs="https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-use-SpeedGrader/ta-p/757",
        lms_reorder_docs="https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-move-or-reorder-an-assignment/ta-p/1289",
        coding_env_name="Google Colab",
        coding_env_origin="https://colab.research.google.com",
        coding_env_kernel_name="runtime",
        assistant_name="Reader",
        assistant_responsibilities="https://docs.google.com/document/d/1NiS1uPM_0OB7dXHP1D90P-XikXj6gwWRUsf0V_dEoUI/edit#heading=h.7f7yn4ehwnkz",
        wait_list="https://www.registrar.columbia.edu/content/wait-lists-ssol",
        registration="https://bulletin.columbia.edu/sipa/registration/",
        cross_registration="https://bulletin.columbia.edu/sipa/registration/#crossregistrationtext",
        auditing="https://www.sipa.columbia.edu/students/student-affairs/academic-advising-faq",
        r_credit="https://www.registrar.columbia.edu/content/grade-options#auditing",
        assignment_cutoff_name="`Until` date",
        python_for_mbas="https://clio.columbia.edu/catalog/15536430",
        statista_url="https://clio.columbia.edu/catalog/11329105",
        final_project_proposal="https://edstem.org",
        attendance_url="https://community.canvaslms.com/t5/Canvas-Basics-Guide/What-is-the-Roll-Call-Attendance-Tool/ta-p/59#take_attendance",
        words=[
            "canvaslms",
            "colab",
            "columbia",
            "courseworks",
            "daqa",
            "python for public policy",
            "reader",
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
        term="Fall 2024",
        lms_name="Brightspace",
        lms_url="https://brightspace.nyu.edu/d2l/home/384630",
        discussions_url="https://brightspace.nyu.edu/d2l/le/lessons/384630/topics/10717594",
        survey_url="https://docs.google.com/forms/d/e/1FAIpQLSeIjidhqviazcLcsgs0rAeIlclFmcQLoxHZgxLhhrNynj5ykw/viewform?usp=sf_link",
        name_tool_url="https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/forms-policies-procedures/pronouns-and-name-pronunciation.html#S1",
        lms_profile_pic_url="https://community.d2l.com/brightspace/kb/articles/18108-change-personal-settings-in-brightspace",
        lms_notification_settings_url="https://brightspace.nyu.edu/d2l/lms/discussions/admin/subscriptions.d2l?ou=384630",
        lms_grading_docs="https://community.d2l.com/brightspace/kb/articles/3529-evaluate-assignments-using-the-assignments-tool",
        lms_reorder_docs="https://community.d2l.com/brightspace/kb/articles/3405-reorder-edit-and-delete-assignments-and-categories",
        coding_env_name="JupyterHub",
        coding_env_origin="https://padmgp-4506-fall.rcnyu.org",
        coding_env_kernel_name="kernel",
        assistant_name="grader",
        assistant_responsibilities="https://docs.google.com/document/d/1dX2MDc5Fhby8GyeKLF4rrI0RZrJAmF1LHGV2SdFIkAE/edit#heading=h.7f7yn4ehwnkz",
        wait_list="https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/albert-help/training/students/registration/waitlists.html",
        registration="https://wagner.nyu.edu/portal/students/academics/registration",
        cross_registration="https://wagner.nyu.edu/portal/students/academics/courses/across-nyu/instructions/form",
        auditing="https://wagner.nyu.edu/portal/students/academics/registration/auditing",
        r_credit="https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/transcripts-certifications-grades/grades.html",
        assignment_cutoff_name="`End Date`",
        python_for_mbas="https://bobcat.library.nyu.edu/permalink/f/ci13eu/nyu_aleph008975996",
        statista_url="https://search.library.nyu.edu/permalink/01NYU_INST/1697t4d/alma990062490650107871",
        final_project_proposal="https://edstem.org/us/courses/68651/discussion/5711987",
        attendance_url="https://community.d2l.com/brightspace/kb/articles/3554-create-and-manage-attendance-registers#enter-attendance-data",
        words=[
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

# text that contains / is adjacent to words above, which are allowed for both schools
EXEMPT = [
    "- [google colab](https://colab.research.google.com/)",
    "anaconda",
    "built around it",  # referring to Colab
    "columbia's graduate school of architecture",  # bio
    "conda activate",
    "conda config",
    "create the environment",
    "dictreader",
    "for row in reader",
    "hannahkates/nyu-python-public-policy",
    "https://community.canvaslms.com/t5/canvas-basics-guide/what-are-grading-schemes/ta-p/41",
    "jupyterhub_url",
    "name: install conda packages",  # CI
    "nbgrader",
    "nyu's quantitative analysis guide",
    "python coding for public policy assignments",
    "secondary",  # matches "conda"
    "set up the reader",
    "speedgrader",  # matches "grader"
    "strict channel priority",  # conda
    "these instructions won't work in colab",
    "upload the notebook to [google colab]",
    "upload the python file to google colab",
    "walk the reader",
]
