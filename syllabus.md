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

## Course Information

- **Course Number:** [INAFU6504](https://vergil.columbia.edu/vergil/course/20251/61319)
- **Course site:** [python-public-policy.afeld.me/en/{{school_slug}}/](https://python-public-policy.afeld.me/en/{{school_slug}}/)
- **Class Meeting Times:** Tuesdays 1/21-3/4
  - Section 1: 9-10:50am ET
  - Section 2: 11-12:50pm ET
- **Class Location:** [International Affairs Building (IAB)](https://goo.gl/maps/uS21RUzpGxxNA4zS6), room 404
- **Prerequisites:** None
- **Textbooks:** None
- Students should bring a laptop to class
  - A tablet with a full keyboard is ok

## Instructor Information

- **Professor:** [Aidan Feldman](https://www.sipa.columbia.edu/communities-connections/faculty/aidan-feldman), alf2215@columbia.edu
- **Readers:**
  - Section 1: Claire Li, ml4981@columbia.edu
  - Section 2: Serena Ye, sy3205@columbia.edu
- **Office Hours:**
  - Mondays 4-5pm ET over [Zoom](https://courseworks2.columbia.edu/courses/210776/external_tools/23749), no appointment necessary
  - Other times by appointment; email the instructor

{% else -%}

## Course Information

- **Course Number:** [PADM-GP 4506](https://wagner.nyu.edu/education/courses/python-coding-for-public-policy)
- **Course site:** [python-public-policy.afeld.me/en/{{school_slug}}/](https://python-public-policy.afeld.me/en/{{school_slug}}/)
- **Class Meeting Times:** Tuesdays 3/18-5/6
  - Section 1: 4:55-6:35pm
  - Section 2: 6:45-8:25pm
- **Class Location:** Wagner, [105 E 17 St](https://maps.app.goo.gl/s96mgESm9W5eEPyUA), room 117
- **Prerequisites:** None
- **Textbooks:** None
- Students should bring a laptop to class
  - A tablet with a full keyboard is ok
  - NYU offers [loaners](https://library.nyu.edu/services/computing/on-campus/laptop-loans/) and [technology support](#technology-support)

## Instructor Information

- **Professor:** [Aidan Feldman](https://wagner.nyu.edu/community/faculty/aidan-feldman), alf9@nyu.edu
- **Grader:** Zixin Guan, zg2622@nyu.edu
- **Office Hours:**
  - Mondays 5-6pm, virtual, no appointment necessary - see Google Calendar invite
  - Other times by appointment; email the instructor

{% endif -%}

## Description

This seven-week course exposes the students to the application and use of Python for data analytics in public policy setting. The course teaches introductory technical programming skills that allow students to learn Python and apply code on pertinent public policy data. The majority of the class content will utilize the [New York City 311 Service Requests](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9) dataset. It's a rich dataset that can be explored from many angles relevant to real-world public policy and program management responsibilities.

Class will be split between:

- Lecture
- Demonstration
- Hands-on time to:
  - Play with the code from lectures
  - Start on the homework
  - Ask questions

{% if id == "nyu" -%}

This class is a prerequisite for [Advanced Data Analytics and Evidence Building](https://wagner.nyu.edu/education/courses/advanced-data-analytics-and-evidence-building), which builds on the topics covered here.

{% endif -%}

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
- How to use [Jupyter](https://jupyter.org/) as a coding environment
- How to work with open data
- How these tools and skills can be leveraged in a policy context

## Schedule

{% if id == "columbia" -%}

| Date | Lecture                                | Homework due                                               | [Late](#assignment-scoring) submission deadline            |
| ---- | -------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| 1/21 | [Intro to coding][l0]                  | none                                                       |                                                            |
| 1/28 | [Working with data][l1]                | [Homework 0][hw0]                                          |                                                            |
| 2/4  | [Manipulating and combining data][l2]  | [Homework 1][hw1]                                          | [Homework 0][hw0]                                          |
| 2/11 | [Data reshaping and visualization][l3] | [Homework 2][hw2]                                          | [Homework 1][hw1]                                          |
| 2/18 | [Dates and time series analysis][l4]   | [Homework 3][hw3] and [Final Project proposal][final_prop] | [Homework 2][hw2]                                          |
| 2/25 | [APIs][l5]                             | [Homework 4][hw4]                                          | [Homework 3][hw3] and [Final Project proposal][final_prop] |
| 3/4  | [The Bigger Picture][l6]               | [Final Project][final]                                     | [Homework 4][hw4]                                          |
| 3/7  | none                                   | none                                                       | [Final Project][final]                                     |
| 3/11 | none                                   | [Final Project peer grading][final-peer]                   |                                                            |

{% else -%}

| Date | Lecture                                | Homework due                                               | [Late](#assignment-scoring)/[resubmission](#resubmission) deadline |
| ---- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------ |
| 3/18 | [Intro to coding][l0]                  | none                                                       |                                                                    |
| 3/25 | none (Spring Break)                    | none                                                       | none                                                               |
| 4/1  | [Working with data][l1]                | [Homework 0][hw0]                                          |                                                                    |
| 4/8  | [Manipulating and combining data][l2]  | [Homework 1][hw1]                                          | [Homework 0][hw0]                                                  |
| 4/15 | [Data reshaping and visualization][l3] | [Homework 2][hw2]                                          | [Homework 1][hw1]                                                  |
| 4/22 | [Dates and time series analysis][l4]   | [Homework 3][hw3] and [Final Project proposal][final_prop] | [Homework 2][hw2]                                                  |
| 4/29 | [APIs][l5]                             | [Homework 4][hw4]                                          | [Homework 3][hw3] and [Final Project proposal][final_prop]         |
| 5/6  | [The Bigger Picture][l6]               | [Final Project][final]                                     | [Homework 4][hw4]                                                  |
| 5/9  | none                                   | none                                                       | [Final Project][final]                                             |
| 5/13 | none                                   | [Final Project peer grading][final-peer]                   |                                                                    |

{% endif -%}

[l0]: https://python-public-policy.afeld.me/en/{{school_slug}}/lecture_0.html
[l1]: https://python-public-policy.afeld.me/en/{{school_slug}}/lecture_1.html
[l2]: https://python-public-policy.afeld.me/en/{{school_slug}}/lecture_2.html
[l3]: https://python-public-policy.afeld.me/en/{{school_slug}}/lecture_3.html
[l4]: https://python-public-policy.afeld.me/en/{{school_slug}}/lecture_4.html
[l5]: https://python-public-policy.afeld.me/en/{{school_slug}}/lecture_5.html
[l6]: https://python-public-policy.afeld.me/en/{{school_slug}}/lecture_6.html

In general, assignments{% if id == "nyu" %} and resubmissions{% endif %} are due at the time class starts. These will all be reflected in the Assignments in [{{lms_name}}]({{lms_url}}).

## Communications

- All assignments will be delivered through [the {{lms_name}} site]({{lms_url}}).
- Assignments, due dates, and other aspects of the course may be modified mid-course.
  - As much advance notice will be given as possible.
- Troubleshooting and other communications between class sessions will be through [Ed Discussions]({{discussions_url}}), so that other students can respond and/or benefit from the answers.
  - Email is also an option, though please only use for questions that aren't appropriate for others to see.
- The instructor/{{assistant_name}} will try to respond within 24 hours, 48 hours max, if someone else hasn't already.

## Assignments and Evaluation

The Course Grade is based on the following:

- [Assignments](#assignment-scoring): 64%
  - [Homework 0][hw0]: 13%
  - [Homework 1][hw1]: 13%
  - [Homework 2][hw2]: 13%
  - [Homework 3][hw3]: 6%
  - [Final Project proposal][final_prop]: 6%
  - [Homework 4][hw4]: 13%
- [Final Project][final]: 20%
- [Final Project peer grading][final-peer]: 5%
- [Attendance](#attendance): 6%
- [Between-Class Participation](#participation): 5%

[hw0]: https://python-public-policy.afeld.me/en/{{school_slug}}/hw_0.html
[hw1]: https://python-public-policy.afeld.me/en/{{school_slug}}/hw_1.html
[hw2]: https://python-public-policy.afeld.me/en/{{school_slug}}/hw_2.html
[hw3]: https://python-public-policy.afeld.me/en/{{school_slug}}/hw_3.html
[hw4]: https://python-public-policy.afeld.me/en/{{school_slug}}/hw_4.html
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

If the submission showed effort, feedback will be given through {% if id == "columbia" %}comments in the notebook{% else %}[annotations in {{lms_name}}](https://www.iup.edu/instructional-design/brightspace-information-hub/add-annotations-to-student-submissions-in-d2l-assignments.html){% endif %}.

#### [Final Project](final_project.md)

The Final Project score will be the [median](https://docs.python.org/3/library/statistics.html#statistics.median) of [peer grades](final_project/peer_grading.md). For the Final Project peer review score, the following apply per review:

- **Minimal feedback:** -10 points
- **Not reviewed:** -20 points

{% if id == "nyu" %}

#### Resubmission

For submissions that showed effort and were on time, the assignment can be resubmitted to improve the score, up to full credit. This will be due before the next class — see the [schedule](#schedule) — and can be resubmitted through {{lms_name}}.
{% endif %}

#### Extensions

Requests for extensions will only be considered if made via email before the deadline, up to [the late submission cutoff shown above](#schedule). Late submission deadlines will only be extended if there is accomodation requested through the school.{% if id == "nyu" %} Resubmission deadlines will not be extended.{% endif %}

### Participation

To encourage cosnsistent, deeper thought about the Assignments, relevance to the broader world, etc., students are expected to do Between-Class Participation. This includes:

- Asking a question of substance
- Answering a question
- Posting a useful/interesting resource
- Sharing an insight

in either:

- Office hours
- [Ed Discussions]({{discussions_url}})
  - When starting a new Conversation, please use a descriptive Title to make them easier to navigate
  - Suggest checking your [notifications settings]({{lms_notification_settings_url}}) to make sure you see conversations that come through
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

Missing class counts as an absence, regardless of the reason or notifying the instructor(s) beforehand. Missing more than 20 minutes of a class session will be treated as an absence. The first absence is treated as a "freebie".

If you do miss class, we trust that it's for a good reason. If you're sick, please use that freebie and stay home and rest.

You are responsible for getting caught up on what was covered in class. You may want to ask a classmate for notes.

### Academic Integrity

If you are copying and pasting from a source (see below), it must be cited. This doesn't need to be in a formal style like APA - a comment (and link, where possible) is fine.

**If you did most of the work yourself, it's ok. If most of the work was copied from elsewhere, it's plagiarism,** and will be reported.

#### Sources

Anything outside of the provided course materials is considered a "source". This includes:

- Other students
- Online resources
- Books
- Generative AI (ChatGPT, Copilot, Gemini, etc.)[\*](#generative-ai)

#### Other notes

- Students are welcome to work with one another, as long as:
  - You indicate who you worked with
  - The submissions are different
- Students are more than welcome to share approaches and code snippets in the Discussions, so long as they aren't giving the full solution away.
- Students may post their [open-ended assignments](assignments/open_ended.md) publicly (on GitHub, LinkedIn, etc). Other assignments (with "correct answers") cannot be posted publicly, to avoid cheating in future semesters. You are more than welcome to share any of your notebooks with specific people, such as future employers.

#### Generative AI

{% if id == "nyu" -%}

This course is taking part in [NYU’s Private Generative AI Service Pilot](https://www.nyu.edu/life/information-technology/artificial-intelligence-at-nyu/private-ai-generative-pilot.html).

**_For the homeworks and Final Project:_**

You are welcome to use [the AI magic](https://python-public-policy.afeld.me/en/{{school_slug}}/assignments.html#generative-ai) and can ask it any questions you like without penalty, but **all use of it must be done through JupyterHub and turned in with the corresponding work**. You can use the same notebook, or a separate one. **All other use of generative AI (through [chatgpt.com](https://chatgpt.com/), [GitHub Copilot](https://github.com/features/copilot), etc.) is prohibited.**

This policy is in place to ensure that:

- The instructor/{{assistant_name}} have a good sense of what generative AI is being used for
- There is a level playing field in terms of the model being used

{% endif -%}

Generative AI tools can be incredibly useful, but the code they provide is often incomplete or wrong. Knowing enough about code to critically interpret their results can turn them from a crutch to a superpower.

{% if id == "columbia" -%}

#### SIPA Academic Integrity Statement

The School of International & Public Affairs does not tolerate cheating or plagiarism in any form. Students who violate the Code of Academic & Professional Conduct will be subject to the Dean's Disciplinary Procedures.

Please familiarize yourself with the proper methods of citation and attribution. The School provides some useful resources online; we strongly encourage you to familiarize yourself with these various styles before conducting research. Cut and paste the following link into your browser to view the Code of Academic & Professional Conduct and to access useful resources on citation and attribution: https://bulletin.columbia.edu/sipa/academic-policies/

Violations of the Code of Academic & Professional Conduct should be reported to the Associate Dean for Student Affairs.

### SIPA Disability Statement

SIPA is committed to ensuring that students registered with Columbia University's Disability Services (DS) receive the reasonable accommodations necessary to participate fully in their academic programs. If you are a student with a disability and have a DS-certified accommodation letter, you may wish to make an appointment with your course instructor to discuss your accommodations. Faculty provide disability accommodations to students with DS-certified accommodation letters, and they provide the accommodations specified in such letters. If you have any additional questions, please contact SIPA's DS liaison at disability@sipa.columbia.edu or 212-854-8690.

{% else -%}

#### Wagner Academic Integrity Statement

Academic integrity is a vital component of Wagner and NYU. All students enrolled in this class are required to read and abide by [Wagner's Academic Code](https://wagner.nyu.edu/portal/students/policies/code). All Wagner students have already read and signed the [Wagner Academic Oath](https://wagner.nyu.edu/portal/students/policies/academic-oath). Plagiarism of any form will not be tolerated and students in this class are expected to report violations to me. If any student in this class is unsure about what is expected of you and how to abide by the academic code, you should consult with me.

### NYU's Calendar Policy on Religious Holidays

[NYU's Calendar Policy on Religious Holidays](https://www.nyu.edu/about/policies-guidelines-compliance/policies-and-guidelines/university-calendar-policy-on-religious-holidays.html) states that members of any religious group may, without penalty, absent themselves from classes when required in compliance with their religious obligations. Please notify me in advance of religious holidays that might coincide with exams to schedule mutually acceptable alternatives.

## Accessibility

Academic accommodations are available for students with disabilities. Please visit the [Moses Center for Student Accessibility](https://www.nyu.edu/life/global-inclusion-and-diversity/centers-and-communities/accessibility.html) website and click on the Reasonable Accommodations and How to Register tab or call or email CSD at (212-998-4980 or mosescsd@nyu.edu) for information. Students who are requesting academic accommodations are strongly advised to reach out to the Moses Center as early as possible in the semester for assistance.

## Technology Support

You have 24/7 support via NYU's IT services. Explore the [NYU servicelink knowledgebase](https://nyu.service-now.com/servicelink/search_results.do?sysparm_search=student+guides&x=0&y=0&sysparm_fa=&sysparm_sp=&sysparm_cat=&sysparm_serv=&sysparm_location=24e7c87598a074004c8c03063d84e2a6&sysparm_role=&sysparm_base=) for troubleshooting and student guides. Contact askIT@nyu.edu or 1-212-998-3333 (24/7) for technology assistance. Your peers are another source of support, so you could ask a friend or classmate for help or tips.

If you do not have the appropriate hardware technology nor financial resources to purchase the technology, consider applying for the NYU [Emergency Relief Grant](https://www.nyu.edu/admissions/financial-aid-and-scholarships/covid-relief-grant.html).

{% endif %}
