# {{assistant_name|title}} guide

_While the {{assistant_name}} is the intended audience here, others are welcome to read it._

## General info

- [Responsibilities section of the job post]({{assistant_responsibilities}})
- [Schedule](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#schedule)
- In grading/Discussions:
  - We want to try giving students _just enough_ hints to figure it out without giving them the answer.
    - If they seem totally lost, direct them to [office hours](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#instructor-information).
  - Don't spend a _ton_ of time trying to figure out something that you don't understand; feel free to escalate to the instructor.
- For students seeking one-on-one help, direct them to [office hours](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#instructor-information).
  - If someone asks to meet with you specifically, you're welcome to do so, but not required.
{% if school_slug == "columbia" -%}
- Notifications:
  - You may want to tweak your [Discussion notification settings](https://edstem.org/us/settings/notifications).
  - You will want to [turn on notifications for assignment comments](https://community.canvaslms.com/t5/Canvas-Question-Forum/Notification-when-student-posts-a-comment-on-an-assignment/m-p/405572#M142680).
{% else -%}
- Log hours for any time you put in related to this class, including any learning you're needing to do yourself to answer questions.
- Subscribe to all the Discussion Topics so you get notified.
{% endif -%}
- Keep an eye out for students who I should encourage to apply as a {{assistant_name}} next term. Things to look for:
  - Being consistently helpful in the Discussions
  - Clean, well-documented solutions for the homeworks
  - Asking good questions

## Weekly cadence

Weeks start/end at the beginning of each class.

{% if school_slug == "columbia" -%}
- Attending class
{% endif -%}
- [Participation](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#participation) tracking{% if school_slug == "columbia" %} for students in your section{% endif %}
  - We can be fairly forgiving/generous with the scoring there
  - Every student should have each week marked one way or the other
  {% if school_slug == "columbia" -%}
  - Each week is represented as an Assignment
    - Easiest to do this through the Grades interface, rather than SpeedGrader
    - Every cell for previous weeks should be filled in
    - Mark each student that participated as Complete
    - Mark those who didn't as Incomplete
  - You can use the Analytics from Ed to help
  - Instructor can [export enrollment activity](https://python-public-policy.afeld.me/en/{{school_slug}}/meta/instructor_guide.html#student-enrollment-activity) for you
    - [We start tracking participation for a student's first full week in the class. Participation for prior weeks should be marked as `Excused`.](https://python-public-policy.afeld.me/en/{{school_slug}}/lecture_0.html#once-you-get-off-the-wait-list)
  {%- endif %}
- Grading assignment submissions and resubmissions and releasing grades for your section
  - Please try and be done with grading of an assignment within four days after it's due (so they have time for resubmission)
  - Feel free to grade things as they come in, in the order received, to give those students more time for resubmission
  - [Info about anonymous grading]({{lms_anonymous_docs}})

### Discussions

{% if school_slug == "columbia" -%}
- [Help page](https://edstem.org/us/help/using-ed-discussion)
{% endif -%}
- We are trying to strike a balance between students getting accurate answers quickly and encouraging students to help one another to cement their learning
- Ensure Discussion questions have answers within [the specified timeline](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#communications).
  {% if school_slug == "columbia" -%}
  - On-call schedule:
    - Mostafa: Monday-Wednesday
    - Kellyann: Thursday-Sunday
  {%- endif %}
  - Wait 24 hours to respond to questions that could be answered by another student, giving them a chance to do so.
    - Make sure homework questions have an answer within 48 hours, since they are time-sensitive.
    - The day before homework is due, answer questions sooner than that to get students unstuck.
- Please give corrections/clarifications on student answers where necessary.
{% if school_slug == "columbia" -%}
- If posts have the wrong Category, are [a Question when they should be a Post](https://edstem.org/us/help/using-ed-discussion#creating-threads) or vice versa, please fix.
- [Mark correct answers as Accepted](https://edstem.org/us/help/using-ed-discussion#accepting-answers), if they aren't already
{%- endif %}

### Check-in meeting

- How's the workload?
- Anything you need clarification on?
- What came up in Discussions/assignments (common problems, etc.) that might be useful to cover in class?

## Assignments

{% if school_slug == "columbia" -%}
- Recommend [creating a GMail filter](https://support.google.com/mail/answer/6579) for something like `from:google.com subject:"shared with you" ("colab notebooks" OR homework)` to `Skip Inbox` so that you aren't notified every time a student shares a notebook with you
- Grading is done through [SpeedGrader](https://community.canvaslms.com/t5/Canvas-Basics-Guide/What-is-SpeedGrader/ta-p/13)
  - Filter the students to your particular section in the top right
  - You can leave comments on particular cells through the Colab interface
  - If points are deducted, explicitly state what the deductions are for
{% else -%}
- Use [annotations](https://brightspaceresources.ccc.edu/kb/how-do-i-use-the-annotation-tool-to-provide-feedback-on-an-assignment-submitted-to-an-assignment-folder/) to leave comments within the PDFs.
{% endif -%}
- [Scoring and regrade rules](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#assignment-scoring)
{% if school_slug == "columbia" -%}
- [How to give extensions](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-assign-an-assignment-to-an-individual-student/ta-p/717#assign_to_student_only)
{% else -%}
- [How to give extensions](https://documentation.brightspace.com/EN/le/assignments/instructor/set_release_conditions.htm?tocpath=Instructors%7CAssess%20and%20grade%20learners%7CCreate%20assignments%20and%20assess%20submissions%7C_____7) — see "Add special access to an assignment"
{%- endif %}
  - Grant any request for 1-2 days made before the deadline; escalate others to the instructor
  - Don't give extensions on the resubmission deadline unless authorized by the instructor
- Solutions folder will be shared with you from Google Drive
  - [Instructor will share them with students](https://python-public-policy.afeld.me/en/{{school_slug}}/assignments.html#submission) via {% if school_slug == "columbia" %}scheduled Announcements{% else %}{{coding_env_name}}{% endif %}
  - The students don't need to match the provided solution exactly, as long as they do what the question is asking
- {{assistant_name|capitalize}} will manually apply [late penalty](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#assignment-scoring)

### Checks

The following should be true for each Assignment:

- [ ] The description is a link to the assignment page on [the site](https://python-public-policy.afeld.me/en/{{school_slug}}/)
- [ ] Points
    - [ ] 100 points per Assignment, potentially split up
    - [ ] Percentage of the overall grade matches [the breakdown in the syllabus](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#assignments-and-evaluation)
- [ ] Grouped in a logical way
- [ ] Display Grade as: Percentage
- [ ] Submission Type: Online, Website URL
- [ ] [Anonymous grading]({{lms_anonymous_docs}})
- [ ] Dates are correct:
  - [ ] Due dates should match the [schedule](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#schedule)
  {% if school_slug == "columbia" -%}
  - [ ] ["Until" date](https://community.canvaslms.com/t5/Instructor-Guide/What-is-the-difference-between-assignment-due-dates-and/ta-p/897) should be the resubmission deadline
    - [ ] Exception is the [Final Project](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project.html), for which we don't accept resubmission
  {% else -%}
  - [ ] End Date should be the Sundays following the Due Date, at the same time
    - [ ] Exception is the [Final Project](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project.html), which should be three days after the Due Date
  {%- endif %}
{% if school_slug == "columbia" -%}
- [ ] [Published](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-publish-or-unpublish-an-assignment-as-an-instructor/ta-p/585)
- [ ] Grading Policy Settings (under Grades tab)
  - [ ] **Late Policies:** Unchecked "Automatically apply deduction to late assignments"
    - [ ] {{assistant_name|capitalize}} will manually deduct late penalty when appropriate (-10% per day)
  - [ ] **Grade Posting Policies:** Automatic
{% else -%}
- [ ] Associated with the `Homework` gradebook category
- [ ] `Visible`
{%- endif %}

### [Final Project](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project.html)

#### Proposals

- Students are encouraged to submit before the deadline to get feedback sooner
  - We aim to turn around feedback on [the proposals](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project.html#proposal) sooner than later, so that students can get started.
- If the proposal shows effort and follows the [format](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project/proposal.html#format), full credit should be given
- Things to look for (don't spend too long on these):
  - Will their dataset answer their question?
  - Do they have a question that is objectively answerable?
  - Will it be the right level of challenge for the duration of the project and their skills, not too much, not too little?
- The feedback you will likely give the most often will be something like:

  > Your question is good, but you'll probably be able to answer it in relatively few lines of code. Think about what your follow-up question(s) will be.

#### Peer review

[The Final Projects themselves are peer graded.](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project/peer_grading.html) Once the peer review deadline passes:

{% if school_slug == "columbia" -%}
1. In the Final Project Assignment, open Speedgrader.
{%- endif %}
1. Open each submission.
1. Calculate the median of the scores from the peers, using that as the final grade.
1. In the Gradebook, give points to the reviewer under the Final Project Peer Review.
   - As long as thoughtful feedback was given, give full points.
