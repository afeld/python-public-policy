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
  {% if school_slug == "columbia" -%}
  - You will want to [turn on notifications for assignment comments](https://community.canvaslms.com/t5/Canvas-Question-Forum/Notification-when-student-posts-a-comment-on-an-assignment/m-p/405572#M142680).
  {%- else %}
- Log hours for any time you put in related to this class, including any learning you're needing to do yourself to answer questions.
{%- endif %}
- Keep an eye out for students who I should encourage to apply as a {{assistant_name}} next term. Things to look for:
  - Being consistently helpful in the Discussions
  - Clean, well-documented solutions for the homeworks
  - Asking good questions

## Weekly cadence

Weeks end the day of class, the next one starts the day after.

{% if school_slug == "columbia" -%}
- Attending class
{% endif -%}
- [Recording attendance]({{attendance_url}}) based on the sign-in sheets
- Grading assignment submissions{% if id == 'nyu' %} and resubmissions{% endif %} and releasing grades for your section
  {% if id == 'columbia' -%}
  - Recommend waiting until the submission deadline to start grading, to avoid issues with students who may have been intending to continue working on it
  {% else -%}
  - Feel free to grade things as they come in, in the order received, to give those students more time for resubmission
  - Please try and be done with grading of an assignment within four days after it's due (so they have time for resubmission)
  {%- endif %}

### [Between-class participation](../syllabus.md#participation) tracking

{% if school_slug == "columbia" %}... for students in your section.{% endif %} [Helper notebook.](ed_helper.ipynb)

- We can be fairly forgiving/generous with what counts as completion
- Every student should have each week marked one way or the other
- The instructor will mark participation for students that came to office hours
- You can use the Analytics from Ed to help
{% if school_slug == "columbia" -%}
- Each week is represented as an Assignment
  - Easiest to do this through the Grades interface, rather than SpeedGrader
  - Every cell for previous weeks should be filled in
  - Mark each student that participated as Complete
  - Mark those who didn't as Incomplete
- Instructor can [export enrollment activity](instructor_guide.md#student-enrollment-activity) for you
  - [We start tracking participation for a student's first full week in the class. Participation for prior weeks should be marked as `Excused`.](../joining_late.md#once-you-join)
{%- endif %}

### [Discussions]({{discussions_url}})

- [Help page](https://edstem.org/us/help/using-ed-discussion)
- We are trying to strike a balance between students getting accurate answers quickly and encouraging students to help one another to cement their learning
- Ensure Discussion questions have answers within [the specified timeline](../syllabus.md#communications).
  {% if school_slug == "columbia" -%}
  - On-call schedule:
    - Sebastian: Monday-Wednesday
    - Leigh: Thursday-Sunday
  {%- endif %}
  - Wait 24 hours to respond to questions that could be answered by another student, giving them a chance to do so.
    - Make sure homework questions have an answer within 48 hours, since they are time-sensitive.
    - Within 24 hours of when homework is due, answer questions as soon as possible to get students unstuck.
- Please give corrections/clarifications on student answers where necessary.
- If posts have the wrong Category, are [a Question when they should be a Post](https://edstem.org/us/help/using-ed-discussion#creating-threads) or vice versa, please fix.
- [Mark correct answers as Accepted](https://edstem.org/us/help/using-ed-discussion#accepting-answers), if they aren't already

### Check-in meeting

- How's the workload?
- Anything you need clarification on?
- Any Discussions the instructor should jump in on?
- What came up in Discussions/assignments (common problems, etc.) that might be useful to cover in class?
- Are all cells in the gradebook filled in (through last week)?

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
- [Scoring {% if school_slug == "nyu" %}and regrade {% endif %}rules](../syllabus.md#assignment-scoring)
{% if school_slug == "columbia" -%}
- [How to give extensions](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-assign-an-assignment-to-an-individual-student/ta-p/717#assign_to_student_only)
{% else -%}
- [How to give extensions](https://documentation.brightspace.com/EN/le/assignments/instructor/set_release_conditions.htm?tocpath=Instructors%7CAssess%20and%20grade%20learners%7CCreate%20assignments%20and%20assess%20submissions%7C_____7) — see "Add special access to an assignment"
{%- endif %}
  - Grant any request for 1-2 days made before the deadline; escalate others to the instructor
  - Set the {{assignment_cutoff_name}} to the original [late submission deadline](../syllabus.md#schedule) or the new due date, whichever is later
  {%- if id == 'nyu' %}
  - Don't give extensions on the resubmission deadline unless authorized by the instructor
  {%- endif %}
- Solutions folder will be shared with you from Google Drive
  - The students don't need to match the provided solution exactly, as long as they do what the question is asking
{%- if id == 'nyu' %}
- {{assistant_name|capitalize}} will manually apply [late penalty](../syllabus.md#assignment-scoring)
{%- endif %}

### Grading

[How to grade in {{lms_name}}]({{lms_grading_docs}})

You are checking student submissions against the solutions. That said, student code/output doesn't need to look _exactly_ like what's in the solution, as long as they're doing what's asked for in each Step.
When grading, points should only be deducted based on [these criteria](../syllabus.md#assignment-scoring). Please leave comments for:

- Point deductions, explaining what it's being deducted for
- Feedback like "this could be done better/differently," even if there isn't a corresponding point deduction

### Checks

The following should be true for each Assignment:

- [ ] The description is a link to the assignment page on this site
- [ ] Points
    - [ ] 100 points per Assignment, except for Homework 3 and the Final Project Proposal which are 50 each
    - [ ] Percentage of the overall grade matches [the breakdown in the syllabus](../syllabus.md#assignments-and-evaluation)
- [ ] Grouped and [ordered]({{lms_reorder_docs}}) in a logical way
- [ ] Display Grade as: Percentage
- [ ] Submission Type: Online, Website URL
{% if school_slug == "nyu" -%}
    - Final Project Proposal is a Discussion
{%- endif %}
- [ ] Dates match [the schedule](../syllabus.md#schedule):
  - [ ] Due date
  - [ ] {{assignment_cutoff_name}}
{% if school_slug == "columbia" -%}
- [ ] [Published](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-publish-or-unpublish-an-assignment-as-an-instructor/ta-p/585)
- [ ] Grading Policy Settings (under Grades tab)
  - [ ] **Late Policies:** Check "Automatically apply deduction to late assignments"
  - [ ] **Grade Posting Policies:** Automatic
{% else -%}
- [ ] Associated with the `Homework` gradebook category
- [ ] `Visible`
{%- endif %}

### Plagiarism

{% if school_slug == "columbia" -%}
Per the [Code of Academic and Professional Conduct](https://bulletin.columbia.edu/sipa/academic-policies/academic-and-professional-conduct/):

> It is the responsibility of all members of the SIPA community to encourage academic integrity and to deter, confront, and report all acts of academic dishonesty.
{%- endif %}

See [the class policies](../syllabus.md#sharing) for more details for what constitues plagiarsm vs. fair reuse.

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
- If the proposal shows effort and follows the [format](../final_project/proposal.md#format), full credit should be given
- Things to look for (don't spend too long on these):
  - Will their dataset answer their question?
  - Do they have a question that is objectively answerable?
  - Will it be the right level of challenge for the duration of the project and their skills, not too much, not too little?
- The feedback you will likely give the most often will be something like:

  > Your question is good, but you'll probably be able to answer it in relatively few lines of code. Think about what your follow-up question(s) will be.

#### Grading

[The Final Projects themselves are peer graded.](../final_project/peer_grading.md) {% if school_slug == "nyu" %}We're using [PeerMark](https://www.nyu.edu/servicelink/KB0018477) to facilitate the peer grading.{% endif %} Once the peer review deadline passes:

{% if school_slug == "columbia" -%}
1. In the Final Project Assignment, open Speedgrader.
{%- endif %}
1. Open each submission.
{% if school_slug == "nyu" -%}
1. For similarity scores over 20%, look at the [report](https://help.turnitin.com/feedback-studio/lti/instructor/instructor-category.htm#the-similarity-report).
   - Matches in data output can be ignored.
   - If it seems like there may be instances of [plagiarism](../syllabus.md#class-policies) or you're not sure, let the instructor know.
{% endif -%}
1. Calculate the median of the scores from the peers, using that as the final grade.
1. In the Gradebook, give points to the reviewer under the Final Project Peer Review.

[Scoring details.](../syllabus.md#final-project)
