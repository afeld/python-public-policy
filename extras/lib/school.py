import dataclasses
from typing import List


@dataclasses.dataclass
class SchoolText:
    """Class to ensure each school has the same configuration structure"""

    id: str
    school_name: str
    school_slug: str
    email: str
    color: str
    course_name: str
    term: str
    lms_name: str
    lms_url: str
    submission_tool_url: str
    discussions_url: str
    survey_url: str
    name_tool_url: str
    lms_profile_pic_url: str
    lms_notification_settings_url: str
    exam_tool_name: str
    exam_tool_docs: str
    grading_docs: str
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
    course_search: str
    linkedin_learning_url: str
    ai_offerings: str
    prefixes: List[str]


SCHOOLS = [
    SchoolText(
        id="columbia",
        school_name="Columbia University",
        school_slug="columbia",
        email="alf2215@columbia.edu",
        color="#201D5D",
        course_name="Python for Public Policy",
        term="Spring 2026",
        lms_name="CourseWorks",
        lms_url="https://courseworks2.columbia.edu/courses/233960",
        submission_tool_url="https://courseworks2.columbia.edu/courses/233960/external_tools/29680?display=borderless",
        discussions_url="https://courseworks2.columbia.edu/courses/233960/external_tools/37606?display=borderless",
        survey_url="https://docs.google.com/forms/d/e/1FAIpQLSdmdpOVWx_jL9vMMmAIeuOgaCkm9Yp5x0qiQiMsSGN8MsnkDA/viewform?usp=dialog",
        name_tool_url="https://courseworks2.columbia.edu/courses/183594/pages/you-at-columbia-a-step-by-step-tutorial",
        lms_profile_pic_url="https://courseworks2.columbia.edu/profile",
        lms_notification_settings_url="https://courseworks2.columbia.edu/profile/communication",
        exam_tool_name="Proctorio",
        exam_tool_docs="https://www.cuit.columbia.edu/proctorio",
        grading_docs="https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-use-SpeedGrader/ta-p/757",
        assistant_name="Reader",
        assistant_responsibilities="https://docs.google.com/document/d/1NiS1uPM_0OB7dXHP1D90P-XikXj6gwWRUsf0V_dEoUI/edit#heading=h.7f7yn4ehwnkz",
        wait_list="https://registrar.columbia.edu/content/class-registration-students",
        registration="https://www.sipa.columbia.edu/sipa-education/bulletin/registration",
        cross_registration="https://www.sipa.columbia.edu/sipa-education/bulletin/registration#how-to-cross-register",
        auditing="https://www.sipa.columbia.edu/sipa-education/bulletin/registration#faq",
        r_credit="https://www.sipa.columbia.edu/sipa-education/bulletin/academic-policies/grading",
        assignment_cutoff_name="`Until` date",
        python_for_mbas="https://clio.columbia.edu/catalog/15536430",
        statista_url="https://clio.columbia.edu/catalog/11329105",
        final_project_proposal="https://edstem.org",
        attendance_url="https://community.canvaslms.com/t5/Canvas-Basics-Guide/What-is-the-Roll-Call-Attendance-Tool/ta-p/59#take_attendance",
        course_search="https://vergil.columbia.edu/",
        linkedin_learning_url="https://www.cuit.columbia.edu/linkedin-learning",
        ai_offerings="https://www.cuit.columbia.edu/content/ai-services",
        prefixes=[
            "canvaslms",
            "columbia",
            "courseworks",
            "daqa",
            "dsp",
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
        email="alf9@nyu.edu",
        color="#57058b",
        course_name="Python Coding for Public Policy",
        term="Fall 2025",
        lms_name="Brightspace",
        lms_url="https://brightspace.nyu.edu/d2l/home/477758",
        submission_tool_url="https://brightspace.nyu.edu/d2l/le/lessons/477758/topics/11846241",
        discussions_url="https://brightspace.nyu.edu/d2l/le/lessons/477758/topics/11846240",
        survey_url="https://docs.google.com/forms/d/e/1FAIpQLSfZI-dMv1-AbZN1bGkfFfrTpWWas6AvIoKoYQuWoNu0uSxefQ/viewform?usp=header",
        name_tool_url="https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/forms-policies-procedures/pronouns-and-name-pronunciation.html#S1",
        lms_profile_pic_url="https://community.d2l.com/brightspace/kb/articles/18108-change-personal-settings-in-brightspace",
        lms_notification_settings_url="https://brightspace.nyu.edu/d2l/Notifications/Settings?ou=477758",
        exam_tool_name="Respondus LockDown Browser",
        exam_tool_docs="https://support.nyu.edu/esc?id=kb_article&sysparm_article=KB0011343",
        grading_docs="https://guides.gradescope.com/hc/en-us/articles/22066635961357-Grading-a-Programming-Assignment#h_01HH372CKNNR01EAMQ1VS6BB7M",
        assistant_name="grader",
        assistant_responsibilities="https://docs.google.com/document/d/1dX2MDc5Fhby8GyeKLF4rrI0RZrJAmF1LHGV2SdFIkAE/edit#heading=h.7f7yn4ehwnkz",
        wait_list="https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/albert-help/training/students/registration/waitlists.html",
        registration="https://wagner.nyu.edu/portal/students/academics/registration",
        cross_registration="https://wagner.nyu.edu/portal/students/academics/courses/across-nyu/instructions/form",
        auditing="https://wagner.nyu.edu/portal/students/academics/registration/auditing",
        r_credit="https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/transcripts-certifications-grades/grades.html",
        assignment_cutoff_name="`Late Due Date`",
        python_for_mbas="https://bobcat.library.nyu.edu/permalink/f/ci13eu/nyu_aleph008975996",
        statista_url="https://search.library.nyu.edu/permalink/01NYU_INST/1697t4d/alma990062490650107871",
        final_project_proposal="https://edstem.org/us/courses/88616/discussion/7308107",
        attendance_url="https://community.d2l.com/brightspace/kb/articles/3554-create-and-manage-attendance-registers#enter-attendance-data",
        course_search="https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/albert-help/training/students/registration/course-search.html",
        linkedin_learning_url="https://www.nyu.edu/life/information-technology/teaching-and-learning-services/instructional-tools/linkedin-learning.html",
        ai_offerings="https://www.nyu.edu/life/information-technology/artificial-intelligence-at-nyu/generative-ai-services.html",
        prefixes=[
            "bonus",
            "brightspace",
            # "conversation",  # Brightspace term, TODO
            "grader",
            "nyu",
            "padm",
            "peerceptiv",
            "python coding for public policy",  # Columbia version doesn't include "Coding"
            "regrad",
            "re-grad",
            "re-submi",
            "turnitin",
            "wagner",
        ],
    ),
]
SCHOOL_TEXT = {school.id: school for school in SCHOOLS}

# text that contains / is adjacent to prefixes above, which are allowed for both schools
EXEMPT = [
    ".zoom.us/rec",
    "autograder",  # matches "grader"
    "baseurl: ",  # _config.yml
    "built around it",  # referring to Colab
    "columbia's graduate school of architecture",  # bio
    "create the environment",
    "dictreader",
    "for row in reader",
    "hannahkates/nyu-python-public-policy",
    "https://community.canvaslms.com/t5/canvas-basics-guide/what-are-grading-schemes/ta-p/41",
    "nyu's quantitative analysis guide",
    "python coding for public policy assignments",
    "set up the reader",
    "speedgrader",  # matches "grader"
    "walk the reader",
]
