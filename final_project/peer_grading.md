# [Final Project](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project.html) peer grading

Your Final Project will be reviewed and graded by three of your peers, and you will grade three others'. The person being graded will be anonymous, but the reviewers won't be. Your score will be the [median](https://docs.python.org/3/library/statistics.html#statistics.median) of the peer grades.

If you disagree with the grade, you can appeal by [emailing the instructor and {{assistant_name}}](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#instructor-information). This comes with a risk: this new grade will be the one that's used, even if it's lower.

## How to review

1. Open [{{lms_name}}]({{lms_url}}).
1. Go to Assignments, then `Final Project`.
{% if school_slug == "columbia" -%}
   - Each submission should appear as a link to `https://colab.research.google.com/drive/...`.
   - If you're unable to access the notebooks, make sure you're signed into Google with your Columbia account, and using that to try and access them. See [these instructions](https://support.google.com/docs/answer/6211862).
{%- endif %}
1. Leave substantive feedback, directly in the notebook and/or as a comment/attachment on the {{lms_name}} Assignment peer review area.
1. Check against [the analysis requirements](https://python-public-policy.afeld.me/en/{{school_slug}}/final_project.html#analysis-requirements), factoring in the applicable [general assignment scoring](https://python-public-policy.afeld.me/en/{{school_slug}}/syllabus.html#assignment-scoring).
   - Explain what points are being deducted for what.
   - State the final score in the comment area of the {{lms_name}} Assignment.

## Notes for reviewers

- Your feedback should include what they did well, as well as what they could do more clearly/simply/etc.
- Points should only be deducted based on the [requirements](#analysis-requirements). A "this could be done better/differently" comment doesn't _necessarily_ need to have a corresponding point deduction.
- You are _not_ expected to run any of their code. The notebook should be graded as-is.
{% if school_slug == "columbia" -%}
- While there are ways to find who owns a notebook on Colab, please avoid doing so.
- "Changes cannot be saved" doesn't apply to comments.
- [Canvas peer review documentation](https://community.canvaslms.com/t5/Student-Guide/How-do-I-submit-a-peer-review-to-an-assignment/ta-p/293)
{% endif -%}
- Reviews are expected to be in-depth, and thus take 15+ minutes each.
- As long as the feedback is thoughtful, you'll receive full points.
