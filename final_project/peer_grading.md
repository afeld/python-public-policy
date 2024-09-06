# [Final Project](../final_project.md) peer grading

Your Final Project will be reviewed and graded by three of your peers, and you will grade three others'. These will be anonymous. [Scoring details.](../syllabus.md#final-project)

If you disagree with the grade, you can appeal by [emailing the instructor and {{assistant_name}}](../syllabus.md#instructor-information). This comes with a risk: this new grade will be the one that's used, even if it's lower.

## How to review

1. Open [{{lms_name}}]({{lms_url}}).
{% if school_slug == "columbia" -%}
1. Go to Assignments, then `Final Project`.
   - Each submission should appear as a link to `https://colab.research.google.com/drive/...`.
   - If you're unable to access the notebooks, try:
      - Removing `authuser=<number>` from the URL, if it contains it
      - Accessing in a browser / [incognito window](https://support.google.com/chrome/answer/95464) where you're only signed into your LionMail account, no other Google accounts.
1. Leave substantive feedback as a comment/attachment in the {{lms_name}} Assignment peer review area.
{% else -%}
1. Go to `Content`, then `Final Project`. You should see an embedded TurnItIn/PeerMark dashboard.
1. Follow [these instructions](https://help.turnitin.com/feedback-studio/d2l/LTI13/student/peermark/writing-a-peer-review.htm).
   - Some students have reported issues when using Safari. If you're unable to access, try a different browser.
   - PeerMark (annoyingly) doesn't let you edit your review after you submit it, so double-check before submitting.
{%- endif %}
1. Check against [the analysis requirements](../final_project.md#analysis-requirements), factoring in the applicable [general assignment scoring](../syllabus.md#assignment-scoring).
1. Explain what points are being deducted for what.
1. State the final score in the comment area.

## Notes for reviewers

- Your feedback should include what they did well, as well as what they could do more clearly/simply/etc.
- The feedback should be constructive; don't be a jerk.
- Points should only be deducted based on the [requirements](../final_project.md#analysis-requirements). Please leave comments beyond that, for things like "this could be done better/differently," even if there isn't a corresponding point deduction.
- You are _not_ expected to run any of their code. The notebook should be graded as-is.
{% if school_slug == "columbia" -%}
- While there are ways to find who owns a notebook on Colab, please avoid doing so.
- "Changes cannot be saved" doesn't apply to comments.
- [Canvas peer review documentation](https://community.canvaslms.com/t5/Student-Guide/How-do-I-submit-a-peer-review-to-an-assignment/ta-p/293)
{% endif -%}
- Reviews are expected to be in-depth, and thus take 15+ minutes each.
- As long as the feedback is thoughtful, you'll receive full points.
