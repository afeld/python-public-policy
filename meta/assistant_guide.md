# {{assistant_name|title}} guide

_While the {{assistant_name}} is the intended audience here, others are welcome to read it._

## General info

- [Responsibilities section of the job post]({{assistant_responsibilities}})
- [Schedule](../syllabus.md#schedule)
- In grading/Discussions:
  - We want to try giving students _just enough_ hints to figure it out without giving them the answer.
    - If they seem totally lost, direct them to [office hours](../syllabus.md#instructor-information).
  - Don't spend a _ton_ of time trying to figure out something that you don't understand; feel free to escalate to the instructor.
- For students seeking one-on-one help, direct them to [office hours](../syllabus.md#instructor-information).
  - If someone asks to meet with you specifically, you're welcome to do so, but not required.
- Notifications:
  - You may want to tweak your [Ed Discussion notification settings](https://edstem.org/us/settings/notifications).
  {% if id == "columbia" -%}
  - You will want to [turn on notifications for assignment comments](https://community.canvaslms.com/t5/Canvas-Question-Forum/Notification-when-student-posts-a-comment-on-an-assignment/m-p/405572#M142680).
  {%- else %}
- Log hours for any time you put in related to this class, including any learning you're needing to do yourself to answer questions.
{%- endif %}
- Keep an eye out for students who I should encourage to apply as a {{assistant_name}} next term. Things to look for:
  - Being consistently helpful in the Discussions
  - Clean, well-documented solutions for the homeworks
  - Asking good questions

## Weekly cadence

Weeks end the day of class, the next one starts the day after. "Weeks" is therefore referring to the class-to-class cycle. These "weeks" may be longer than seven days if there's no lecture due to a holiday.

{% if id == "columbia" -%}
- Attending class
{% else -%}
- While you aren't expected to attend class in general, you are more than welcome to join for [the guest lecture](../syllabus.md#schedule).
{% endif -%}
- [Recording attendance]({{attendance_url}}) based on the sign-in sheets
  - [Attendance policy](../syllabus.md#attendance)
  {% if id == "columbia" -%}
  - Please arrive to class a bit early to sit with the attendance sheet as people walk in.
    - This is to ensure that people are only signing for themselves.
  - 20 minutes into the lecture, please put the sheet away. Students who arrive after that are considered absent.
  - Please hold onto a copy/photo of the attendance sheets, in case we need to reference the signatures later.
  {%- endif %}
- Grading assignment submissions and releasing grades for your section
  {% if id == "columbia" -%}
  - Recommend waiting until the submission deadline to start grading, to avoid issues with students who may have been intending to continue working on it
  {%- endif %}

### [Between-class participation](../syllabus.md#participation) tracking

{% if id == "columbia" %}... for students in your section.{% endif %} [Helper notebook.](ed_helper.ipynb)

- There are five weeks of participation tracked, from [Lecture 0 through Lecture 5](../syllabus.md#schedule).
  - That last week, they should be focused on their [Final Project](../final_project.md).
- We can be fairly forgiving/generous with what counts as completion.
- Every student should have each week marked one way or the other.
- The instructor will mark participation for students that came to office hours.
- Each week is represented as {% if id == "columbia" %}an Assignment{% else %}a gradebook item{% endif %}.
  {% if id == "columbia" -%}
  - Easiest to do this through the Grades interface, rather than SpeedGrader.
  {%- endif %}
  - Every cell for previous weeks should be filled in.
  - Mark each student that participated as {% if id == "columbia" %}Complete{% else %}`P` (present){% endif %}.
  - Mark those who didn't as {% if id == "columbia" %}Incomplete{% else %}`A` (absent){% endif %}.
{% if id == "columbia" -%}
- Instructor can [export enrollment activity](instructor_guide.md#student-enrollment-activity) for you.
  - [We start tracking participation for a student's first full week in the class. Participation for prior weeks should be marked as `Excused`.](../joining_late.md#once-you-join)
{%- endif %}

### [Discussions]({{discussions_url}})

- [Help page](https://edstem.org/us/help/using-ed-discussion)
- We are trying to strike a balance between students getting accurate answers quickly and encouraging students to help one another to cement their learning.
- Ensure Discussion questions have answers within [the specified timeline](../syllabus.md#communications).
  {% if id == "columbia" -%}
  - Discussion monitoring schedule:
    - Sunday-Tuesday: Claire
    - Wednesday-Saturday: Serena
  {%- endif %}
  - Wait 24 hours to respond to questions that could be answered by another student, giving them a chance to do so.
    - Make sure homework questions have an answer within 48 hours, since they are time-sensitive.
    - Within 24 hours of when homework is due, answer questions as soon as possible to get students unstuck.
- Please give corrections/clarifications on student answers where necessary.
- If posts have the wrong Category, are [a Question when they should be a Post](https://edstem.org/us/help/using-ed-discussion#creating-threads) or vice versa, please fix.
- [Mark correct answers as Accepted](https://edstem.org/us/help/using-ed-discussion#accepting-answers), if they aren't already.

### Check-in meeting

- How's the workload?
- Anything you need clarification on?
- Any Discussions the instructor should jump in on?
- What came up in Discussions/assignments (common problems, etc.) that might be useful to cover in class?
- Are all cells in the gradebook filled in (through last week)?

## Assignments

It's recommended that you [create a GMail filter](https://support.google.com/mail/answer/6579) for something like `from:google.com subject:"shared with you" ("colab notebooks" OR homework)` to `Skip Inbox` so that you aren't notified every time a student shares a notebook with you.

### Checks

The following should be true for each Assignment:

- [ ] The description is a link to the assignment page on this site
- [ ] Points
    - [ ] 100 points per Assignment, except for Homework 3 and the Final Project Proposal which are 50 each
    - [ ] Percentage of the overall grade matches [the breakdown in the syllabus](../syllabus.md#assignments-and-evaluation)
{% if id == "columbia" -%}
- [ ] Grouped and [ordered](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-move-or-reorder-an-assignment/ta-p/1289) in a logical way
- [ ] Display Grade as: Percentage
- [ ] Submission Type: Online, Website URL
    - Final Project Proposal is a Discussion
- [ ] Dates match [the schedule](../syllabus.md#schedule):
  - [ ] Due date
  - [ ] {{assignment_cutoff_name}}
- [ ] [Published](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-publish-or-unpublish-an-assignment-as-an-instructor/ta-p/585)
- [ ] Grading Policy Settings (under Grades tab)
  - [ ] **Late Policies:** Check "Automatically apply deduction to late assignments"
  - [ ] **Grade Posting Policies:** Automatic
{% else -%}
- [ ] `Allow late submissions`
- [ ] Dates match [the schedule](../syllabus.md#schedule):
  - [ ] `Release Date` is the start of the course
  - [ ] `Due Date`
    - Use the start of the second section, if applicable.
  - [ ] {{assignment_cutoff_name}}
    - Ditto.
- [ ] `Enable manual grading`
- [ ] `Submission Methods Enabled`: `Upload` only
- [ ] It's officially ["linked"](https://support.nyu.edu/esc?id=kb_article&sysparm_article=KB0012083) from {{lms_name}}
- [ ] It shows up in the {{lms_name}} Gradebook properly
{%- endif %}

### Grading

[Official docs](https://guides.gradescope.com/hc/en-us/articles/22066635961357-Grading-a-Programming-Assignment#h_01HH372CKNNR01EAMQ1VS6BB7M)

- If points are deducted, explicitly state what the deductions are for.
- If you're having trouble accessing the notebook in Google Colab, make sure the URL doesn't include an `authuser` [parameter](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL#parameters).
- [Scoring {% if id == "nyu" %}and regrade {% endif %}rules](../syllabus.md#assignment-scoring)
- You are checking student submissions against the solutions. That said, student code/output doesn't need to look _exactly_ like what's in the solution, as long as they're doing what's asked for in each Step.
When grading, points should only be deducted based on [these criteria](../syllabus.md#assignment-scoring). Please leave comments for:
  - Point deductions, explaining what it's being deducted for
  - Feedback like "this could be done better/differently," even if there isn't a corresponding point deduction
- [How to give extensions](https://guides.gradescope.com/hc/en-us/articles/22251762857997-Extending-assignment-release-dates-due-dates-and-time-limits)
  - Grant any request for 1-2 days made before the deadline; escalate others to the instructor.
  - Set the {{assignment_cutoff_name}} to the original [late submission deadline](../syllabus.md#schedule) or the new due date, whichever is later.
- Solutions folder will be shared with you from Google Drive
  - The students don't need to match the provided solution exactly, as long as they do what the question is asking.
- Per Gradescope support, "Unfortunately, there isn't a way right now to assign "0" scores to all students without submissions on Gradescope. For now, the workaround would be to upload a blank/fake submission for each of the students who didn't submit anything for the assignment on Gradescope and grade those submissions with a 0 score for all questions, so that the students have a 0 on Gradescope." [Feature request.](https://portal.productboard.com/sz44uvlbbmnviv939g6lvnkd/c/119-instructors-can-give-students-without-submissions-0-scores-on-gradescope)
- Note that you need to both `Post Grades` and [`Publish Grades`](https://guides.gradescope.com/hc/en-us/articles/22067099093517-Reviewing-Grades#h_01HRFQT3293V5J0QA8D6ZETGVJ).
- {{assistant_name|capitalize}} will manually apply [late penalty](../syllabus.md#assignment-scoring)

### Plagiarism

{% if id == "columbia" -%}
Per the [Code of Academic and Professional Conduct](https://bulletin.columbia.edu/sipa/academic-policies/academic-and-professional-conduct/):

> It is the responsibility of all members of the SIPA community to encourage academic integrity and to deter, confront, and report all acts of academic dishonesty.
{%- endif %}

See [the class policies](../syllabus.md#academic-integrity) for more details for what constitues plagiarism vs. fair reuse.

It isn't your responsibility to look for potential instances of cheating/plagiarism. That said, if you have suspicions of those occuring, you must report them to the instructor. Things you might notice:

- Use of a package we haven't covered in class
- Using a technique we didn't cover in class
- Multiple student submisions:
  - Being identical
  - Solving a problem in the same unusual way

### [Final Project](../final_project.md)

#### Proposals

- Students are encouraged to submit before the deadline to get feedback sooner.
  - Please provide feedback on [the proposals](../final_project/proposal.md) within four days of submission so that students can get started.
- If the proposal shows effort and follows the [format](../final_project/proposal.md#format), full credit should be given.
- Things to look for (don't spend too long on these):
  - Will their dataset answer their question?
  - Do they have a question that is objectively answerable?
  - Will it be the right level of challenge for the duration of the project and their skills, not too much, not too little?
- You will often need to provide feedback along the lines of:

  > Your question is good, but you'll probably be able to answer it in relatively few lines of code. Think about what your follow-up question(s) will be.

- Constructive feedback can be given as a reply in Ed (where other students can see). If the proposal is bad, send an email.
  - In other words, avoid embarrassing anyone.
- To indicate to a student that their proposal is good to go, mark the reply as [Resolved](https://edstem.org/help/using-ed-discussion).

#### Grading

[The Final Projects themselves are peer graded.](../final_project/peer_grading.md) {% if id == "nyu" %}We're using [Peerceptiv](https://support.nyu.edu/esc?id=kb_article&sysparm_article=KB0012161) to facilitate the peer grading.{% endif %} Once the peer review deadline passes:

{% if id == "columbia" -%}
1. In the Final Project Assignment, open Speedgrader.
{%- endif %}
1. Open each submission.
{% if id == "nyu" -%}
1. For similarity scores over 20%, look at the [report](https://guides.turnitin.com/hc/en-us/articles/23438306524173-Navigating-the-Similarity-Report).
   - Matches in data output can be ignored.
   - If it seems like there may be instances of [plagiarism](../syllabus.md#class-policies) or you're not sure, let the instructor know.
{% endif -%}
1. Calculate the median of the scores from the peers, using that as the final grade.
1. In the Gradebook, give points to the reviewer under the Final Project Peer Review.

[Scoring details.](../syllabus.md#final-project)

{% if id == "columbia" -%}
## Final grades

To compute the [attendance](../syllabus.md#attendance) score:

1. [Export the Roll Call attendance data.](https://community.canvaslms.com/t5/Canvas-Basics-Guide/What-is-the-Roll-Call-Attendance-Tool/ta-p/59#export_attendance_data)
1. Copy [the script](https://github.com/afeld/python-public-policy/blob/main/extras/scripts/attendance.py) into Google Colab.
1. Adjust the constants at the top as necessary.
1. Run the code.
{%- endif %}
