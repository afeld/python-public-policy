{% if id == "columbia" -%}
[![Columbia SIPA banner](extras/img/sipa.svg)](https://www.sipa.columbia.edu/)

---

{% else -%}

[![NYU Wagner banner](https://wagner.nyu.edu/files/contact/img/Plain-Header.jpg)](https://wagner.nyu.edu)

{% endif -%}

# Syllabus

<p style="font-size: 2rem; font-weight:bold; text-align: center;">{{course_name}} - {{term}}</p>

<div class="print-only">See up-to-date version of this syllabus at <a href="https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html">python-public-policy.afeld.me</a>.</div>
<style>
  .print-only {
    display: none;
  }
  @media print {
    .print-only {
      display: block;
    }
  }
</style>

{% if id == "columbia" -%}

This is the syllabus for the Spring editions of the course. [Find information about the Fall editions (SIPA6650IA) in Vergil.](https://vergil.columbia.edu/vergil/course/20261/105959)

## Course Information

- **Course Number:** [SIPA6650IA](https://vergil.columbia.edu/vergil/course/20261/105959), formerly [INAFU6504](https://vergil.columbia.edu/vergil/course/20251/61319)
- **Course site:** [python-public-policy.afeld.me/en/{{school_slug}}/](https://python-public-policy.afeld.me/en/{{school_slug}}/)
- **Class Meeting Times:** Tuesdays 1/20-3/3
  - Section 1: 10-11:50am ET
  - Section 2: 1:10-3pm ET
- **Class Location:** [International Affairs Building (IAB)](https://goo.gl/maps/uS21RUzpGxxNA4zS6), room 403
- **Prerequisites:** None
- **Textbooks:** None
- Students should bring a laptop to class
  - A tablet with a full keyboard is ok

## Instructor Information

- **Professor:** [Aidan Feldman](https://www.sipa.columbia.edu/communities-connections/faculty/aidan-feldman), {{email}}
- **Readers:**
  - Section 1: Pranav Mehta, pm3313@columbia.edu
  - Section 2: Xinran (Sara) Yang, sxy2007@columbia.edu
- **Office Hours:**
  - Mondays 5-6pm over [Zoom](https://courseworks2.columbia.edu/courses/233960/external_tools/72338), no appointment necessary
  - Other times by appointment; email the instructor

{% else -%}

## Course Information

- **Course Number:** [PADM-GP 4506](https://wagner.nyu.edu/education/courses/python-coding-for-public-policy)
- **Course site:** [python-public-policy.afeld.me/en/{{school_slug}}/](https://python-public-policy.afeld.me/en/{{school_slug}}/)
- **Class Meeting Times:** Wednesdays, 10/22-12/10, 6:45-8:25pm
- **Class Location:** Wagner, [105 E 17 St](https://maps.app.goo.gl/s96mgESm9W5eEPyUA), room 115
- **Prerequisites:** None
- **Textbooks:** None
- Students should bring a laptop to class
  - A tablet with a full keyboard is ok
  - NYU offers [loaners](https://library.nyu.edu/services/computing/on-campus/laptop-loans/) and [technology support](#technology-support)

## Instructor Information

- **Professor:** [Aidan Feldman](https://wagner.nyu.edu/community/faculty/aidan-feldman), {{email}}
- **Office Hours:** By appointment; email the instructor

{% endif -%}

## Description

Alternate title: "How to Use a Bit of Code to Do Things That Would Be Really Hard in Spreadsheets." Students will learn data analysis through the Python programming language — exploring, manipulating, visualizing, and interpreting open data to answer policy questions. The class incorporates use of generative AI for coding problems, helping students understand its strengths and weaknesses. No coding experience required.

## Homework

Homework assignments will consist of two different formats:

1. **Online tutorials:** In advance of classes, online tutorials will be assigned as homework. These online tutorials will introduce students to critical Python concepts. The following lecture will then focus on applying those concepts to real public policy data questions.
1. **Coding:** Students will complete Python coding exercises that apply new concepts they have learned in lecture. Coding assignments will build off of concepts covered in previous assignments.

These are expected to take 5-10 hours per week.

## Learning Objectives

By the end of the course, students will know:

- Python fundamentals
  - Common data types
  - Functions
  - Reading technical documentation
  - Troubleshooting
- How to use [pandas](https://pandas.pydata.org/) and other packages for data exploration, manipulation, visualization, and analysis
- How to use a (Jupyter) notebook coding environment
- How to work with open data
- How these tools and skills can be leveraged in a policy context

## Schedule

{% if id == "columbia" -%}

| Date  | Lecture          | Homework due                                               | [Late](#assignment-scoring) submission deadline            |
| ----- | ---------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| 1/20  | {doc}`lecture_0` | none                                                       |                                                            |
| 1/27  | {doc}`lecture_1` | [Homework 0][hw0]                                          |                                                            |
| 2/3   | {doc}`lecture_2` | [Homework 1][hw1]                                          | [Homework 0][hw0]                                          |
| 2/10  | {doc}`lecture_3` | [Homework 2][hw2]                                          | [Homework 1][hw1]                                          |
| 2/17  | {doc}`lecture_4` | [Homework 3][hw3] and [Final Project proposal][final_prop] | [Homework 2][hw2]                                          |
| 2/24  | {doc}`lecture_5` | [Homework 4][hw4]                                          | [Homework 3][hw3] and [Final Project proposal][final_prop] |
| 3/3   | {doc}`lecture_6` | [Final Project][final]                                     | [Homework 4][hw4]                                          |
| 3/6   | none             | none                                                       | [Final Project][final]                                     |
| 3/9\* | [Exam][exam]     |                                                            |                                                            |
| 3/10  | none             | [Final Project peer grading][final-peer]                   |                                                            |

\*This is a Monday, same [time slots](#course-information).

{% else -%}

| Date  | Lecture             | Homework due                                               | [Late deadline](#assignment-scoring)                       |
| ----- | ------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| 10/22 | {doc}`lecture_0`    | none                                                       |                                                            |
| 10/29 | {doc}`lecture_1`    | [Homework 0][hw0]                                          |                                                            |
| 11/5  | {doc}`lecture_2`    | [Homework 1][hw1]                                          | [Homework 0][hw0]                                          |
| 11/12 | {doc}`lecture_3`    | [Homework 2][hw2]                                          | [Homework 1][hw1]                                          |
| 11/19 | {doc}`lecture_4`    | [Homework 3][hw3] and [Final Project proposal][final_prop] | [Homework 2][hw2]                                          |
| 11/26 | none (Thanksgiving) | none                                                       | [Homework 3][hw3] and [Final Project proposal][final_prop] |
| 12/3  | {doc}`lecture_5`    | [Homework 4][hw4]                                          | none                                                       |
| 12/10 | {doc}`lecture_6`    | [Final Project][final]                                     | [Homework 4][hw4]                                          |
| 12/13 | none                | none                                                       | [Final Project][final]                                     |
| 12/17 | [Exam][exam]        | [Final Project peer grading][final-peer]                   |                                                            |

{% endif -%}

In general, assignments are due at the time class starts. These will all be reflected in the Assignments in [Gradescope]({{submission_tool_url}}).

## Communications

- Assignments, due dates, and other aspects of the course may be modified mid-course.
  - As much advance notice will be given as possible.
- Troubleshooting and other communications between class sessions will be through [Ed Discussion]({{discussions_url}}), so that other students can respond and/or benefit from the answers.
  - Email is also an option, though please only use for questions that aren't appropriate for others to see.
- The instructor/{{assistant_name}} will try to respond within 24 hours, 48 hours max, if someone else hasn't already.

## Assignments and Evaluation

The Course Grade is based on the following:

- [Assignments](#assignment-scoring): 50%
  - [Homework 0][hw0]: 10%
  - [Homework 1][hw1]: 10%
  - [Homework 2][hw2]: 10%
  - [Homework 3][hw3]: 5%
  - [Final Project proposal][final_prop]: 5%
  - [Homework 4][hw4]: 10%
- [Exam][exam]: 14%
- [Final Project][final]: 20%
- [Final Project peer grading][final-peer]: 5%
- [Attendance](#attendance): 6%
- [Between-Class Participation](#participation): 5%

[hw0]: https://python-public-policy.afeld.me/en/{{school_slug}}/hw_0.html
[hw1]: https://python-public-policy.afeld.me/en/{{school_slug}}/hw_1.html
[hw2]: https://python-public-policy.afeld.me/en/{{school_slug}}/hw_2.html
[hw3]: https://python-public-policy.afeld.me/en/{{school_slug}}/hw_3.html
[hw4]: https://python-public-policy.afeld.me/en/{{school_slug}}/hw_4.html
[exam]: https://python-public-policy.afeld.me/en/{{school_slug}}/exam.html
[final_prop]: https://python-public-policy.afeld.me/en/{{school_slug}}/final_project/proposal.html
[final]: https://python-public-policy.afeld.me/en/{{school_slug}}/final_project.html
[final-peer]: https://python-public-policy.afeld.me/en/{{school_slug}}/final_project/peer_grading.html

{% if id == "columbia" -%}
The overall grade is curved; see [the methodology](https://python-public-policy.afeld.me/en/{{school_slug}}/curve.html).
{% else -%}
It is entirely possible for everyone in the class to get over 100%.
{%- endif %}

### Assignment scoring

- **Late work:** {% if id == "columbia" %}-10%{% else %}-10 points{% endif %} per day
- **Syntax errors:** -10 points
- **Incomplete Steps / Steps with logic errors:** -2 to -5 points
- [**Visualizations incomplete, e.g. missing meaningful title/labels:**](https://python-public-policy.afeld.me/en/{{school_slug}}/lecture_3.html#chart-hygiene) -3 points
- **Unattempted Steps:** -10 points
- **Homework [1](hw_1.md)/[4](hw_4.md) doesn't [read like a blog post](assignments/open_ended.md#read-like-a-blog-post):** -10 to -20 points

If the submission showed effort, written feedback will be provided through Gradescope.

#### [Final Project](final_project.md)

The Final Project score will be the [median](https://docs.python.org/3/library/statistics.html#statistics.median) of [peer grades](final_project/peer_grading.md). For the Final Project peer review score, the following apply per review:

- **Minimal feedback:** -10 points
- **Not reviewed:** -20 points

#### Extensions

Requests for extensions will only be considered if made via email before the deadline, up to [the late submission cutoff shown above](#schedule). Late submission deadlines will only be extended if there is accomodation requested through the school.

### Participation

To encourage consistent, deeper thought about the Assignments, relevance to the broader world, etc., students are expected to do Between-Class Participation. This includes:

- Asking a question of substance
- Answering a question
- Posting a useful/interesting resource
- Sharing an insight

in either:

- Office hours
- [Ed Discussion]({{discussions_url}})
  - When starting a new Conversation, please use a descriptive Title to make them easier to navigate.
- Email

A student's overall Between-Class Participation score is calculated based on some form of participation every week. The following don't count:

- In-class participation, due to:
  - The difficuly of tracking participation live
  - Some students being more shy
- Homework revisions
- Communications about grades or other administrivia

### Letter Grades

Letter grades for the entire course will be assigned as follows:

| Letter Grade | GPA Points | Description | Criteria                                                                                                                                                                                                                                                                                                                                                                   |
| ------------ | ---------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A            | 4.0 points | Excellent   | Exceptional work for a graduate student. Work at this level is unusually thorough, well-reasoned, creative, methodologically sophisticated, and well written. Work is of exceptional, professional quality.                                                                                                                                                                |
| A-           | 3.7 points | Very good   | Very strong work for a graduate student. Work at this level shows signs of creativity, is thorough and well-reasoned, indicates strong understanding of appropriate methodological or analytical approaches, and meets professional standards.                                                                                                                             |
| B+           | 3.3 points | Good        | Sound work for a graduate student; well-reasoned and thorough, methodologically sound. This is the graduate student grade that indicates the student has fully accomplished the basic objectives of the course.                                                                                                                                                            |
| B            | 3.0 points | Adequate    | Competent work for a graduate student even though some weaknesses are evident. Demonstrates competency in the key course objectives but shows some indication that understanding of some important issues is less than complete. Methodological or analytical approaches used are adequate but student has not been thorough or has shown other weaknesses or limitations. |
| B-           | 2.7 points | Borderline  | Weak work for a graduate student; meets the minimal expectations for a graduate student in the course. Understanding of salient issues is somewhat incomplete. Methodological or analytical work performed in the course is minimally adequate. Overall performance, if consistent in graduate courses, would not suffice to sustain graduate status in "good standing."   |
| C+           | 2.3 points | Deficient   | Inadequate work for a graduate student; does not meet the minimal expectations for a graduate student in the course. Work is inadequately developed or flawed by numerous errors and misunderstanding of important issues. Methodological or analytical work performed is weak and fails to demonstrate knowledge or technical competence expected of graduate students.   |
| C            | 2.0 points | "           | "                                                                                                                                                                                                                                                                                                                                                                          |
| C-           | 1.7 points | "           | "                                                                                                                                                                                                                                                                                                                                                                          |
| F            | 0.0 points | Fail        | Work fails to meet even minimal expectations for course credit for a graduate student. Performance has been consistently weak in methodology and understanding, with serious limits in many areas. Weaknesses or limits are pervasive.                                                                                                                                     |

## Class Policies

- All submissions must be made from a Jupyter notebook file, following [these instructions](https://python-public-policy.afeld.me/en/{{school_slug}}/assignments.html).

### Attendance

Attending class is mandatory, but most importantly, important. Learning programming requires commitment from the part of the student and the skills are built out of practice. If you miss an experience in class, you miss an important learning moment and the class misses your contribution.

Missing class counts as an absence, regardless of the reason or notifying the instructor(s) beforehand. Missing more than 20 minutes of a class session will be treated as an absence. The first absence is treated as a "freebie". Your final Attendance score will be calculated as:

$$\text{maximum_score} = \text{total_classes} - \text{freebies} = 7 - 1 = 6$$

$$\text{your_score} = \min(\text{maximum_score}, \text{number_of_classes_you_attended})$$

If you do miss class, we trust that it's for a good reason. If you're sick, please use that freebie and stay home and rest.

You are responsible for getting caught up on what was covered in class. You may want to ask a classmate for notes.

### Devices

To encourage focus and participation, students are asked to keep laptops closed and phones away in lecture by default. (Accommodations for students with disabilities are an exception.) You'll be asked to open the laptops for in-class exercises.

### Academic Integrity

If you are copying and pasting from a source (see below), it must be cited. This doesn't need to be in a formal style like APA - a comment (and link, where possible) is fine.

**If you did most of the work yourself, it's ok. If most of the work was copied from elsewhere, it's plagiarism,** and will be reported.

#### Sources

Anything outside of the provided course materials is considered a "source". This includes:

- Other students
- Online resources
- Books
- Generative AI (ChatGPT, Claude, Copilot, Gemini, etc.)

#### Other notes

- Students are welcome to work with one another, as long as:
  - You indicate who you worked with
  - The submissions are different
- Students are more than welcome to share approaches and code snippets in the Discussions, so long as they aren't giving the full solution away.
- Students may post their [open-ended assignments](assignments/open_ended.md) publicly (on GitHub, LinkedIn, etc). Other assignments (with "correct answers") cannot be posted publicly, to avoid cheating in future semesters. You are more than welcome to share any of your notebooks with specific people, such as future employers.
- [Tips for working with generative AI](https://python-public-policy.afeld.me/en/{{school_slug}}/assignments.html#generative-ai)

{% if id == "columbia" -%}

#### SIPA Academic Integrity Statement

The School of International & Public Affairs does not tolerate cheating or plagiarism in any form. Students who violate the Code of Academic & Professional Conduct will be subject to the Dean’s Disciplinary Procedures. Familiarize yourself with proper citation methods using the resources available online at https://www.sipa.columbia.edu/sipa-education/bulletin/academic-policies. Report violations to the Associate Dean for Student Affairs.

### SIPA Disability Statement

SIPA is committed to providing reasonable accommodations for students registered with Columbia University's Disability Services (DS). Students with DS-certified accommodation letters should discuss their accommodations with their instructor. Contact SIPA’s DS liaison for additional questions: disability@sipa.columbia.edu or 212-854-8690.

{% else -%}

#### Wagner Academic Integrity Statement

Academic integrity is a vital component of Wagner and NYU. All students enrolled in this class are required to read and abide by [Wagner's Academic Code](https://wagner.nyu.edu/portal/students/policies/code). All Wagner students have already read and signed the [Wagner Academic Oath](https://wagner.nyu.edu/portal/students/policies/academic-oath). Plagiarism of any form will not be tolerated and students in this class are expected to report violations to me. If any student in this class is unsure about what is expected of you and how to abide by the academic code, you should consult with me.

### NYU's Calendar Policy on Religious Holidays

[NYU's Calendar Policy on Religious Holidays](https://www.nyu.edu/about/policies-guidelines-compliance/policies-and-guidelines/university-calendar-policy-on-religious-holidays.html) states that members of any religious group may, without penalty, absent themselves from classes when required in compliance with their religious obligations. Please notify me in advance of religious holidays that might coincide with exams to schedule mutually acceptable alternatives.

## Accessibility

Academic accommodations are available for students with disabilities. Please visit the [Moses Center for Accessibility and Inclusive Culture website](https://www.nyu.edu/life/community-flourishing/centers-and-communities/accessibility.html) and follow the steps outlined on that page to request an accommodation. You can also email the Moses Center (<mosescenter@nyu.edu>) for information. Students who are requesting academic accommodations are strongly advised to reach out to the Moses Center as early as possible in the semester for assistance.

## Technology Support

You have 24/7 support via NYU's IT services. Explore the [NYU servicelink knowledgebase](https://nyu.service-now.com/servicelink/search_results.do?sysparm_search=student+guides&x=0&y=0&sysparm_fa=&sysparm_sp=&sysparm_cat=&sysparm_serv=&sysparm_location=24e7c87598a074004c8c03063d84e2a6&sysparm_role=&sysparm_base=) for troubleshooting and student guides. Contact askIT@nyu.edu or 1-212-998-3333 (24/7) for technology assistance. Your peers are another source of support, so you could ask a friend or classmate for help or tips.

If you do not have the appropriate hardware technology nor financial resources to purchase the technology, consider applying for the NYU [Emergency Relief Grant](https://www.nyu.edu/admissions/financial-aid-and-scholarships/covid-relief-grant.html).

{% endif %}
