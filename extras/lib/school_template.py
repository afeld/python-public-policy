import re
import dataclasses
from urllib.parse import urlencode
from jinja2 import Environment, StrictUndefined
from nbconvert.preprocessors import Preprocessor
from nbformat import NotebookNode
from traitlets import Unicode

from .school import EXEMPT, SCHOOL_TEXT, SCHOOLS, SchoolText

COURSE_HOSTNAME = "python-public-policy.afeld.me"

env = Environment(
    undefined=StrictUndefined,
    autoescape=False,
)


def nbgitpuller_url(origin: str):
    """https://nbgitpuller.readthedocs.io/en/latest/topic/url-options.html"""

    query = urlencode(
        {
            "repo": "https://github.com/afeld/python-public-policy",
            "urlpath": "tree/python-public-policy/",
            "branch": "nyu",
        }
    )
    return f"{origin}/hub/user-redirect/git-pull?{query}"


def get_vars(school_id: str):
    school_text = SCHOOL_TEXT[school_id]
    local_vars = dataclasses.asdict(school_text)

    origin = local_vars["coding_env_origin"]
    if school_id == "nyu":
        local_vars["coding_env_url"] = nbgitpuller_url(origin)
    else:
        local_vars["coding_env_url"] = origin

    return local_vars


def render_template(source: str, school_id: str):
    template = env.from_string(source)
    local_vars = get_vars(school_id)
    return template.render(**local_vars)


def check_line(line: str, line_num: int, this_school: SchoolText):
    lower_line = line.lower()
    for exemption in EXEMPT:
        if exemption in lower_line:
            return

    other_schools = [
        other_school for other_school in SCHOOLS if other_school.id != this_school.id
    ]
    for other_school in other_schools:
        for prefix in other_school.prefixes:
            msg = f'"{prefix}" found, line {line_num}:\n\n{line}\n'
            assert re.search(rf"\b{prefix}", line, re.IGNORECASE) is None, msg

    # site check
    if COURSE_HOSTNAME in line:
        # (imperfectly) assure it's linking to the right version
        assert f"{COURSE_HOSTNAME}/en/{this_school.school_slug}" in line, (
            f"Not properly linking to course site, line {line_num}:\n\n{line}\n"
        )


def confirm_no_jinja_tags(source: str):
    for i, line in enumerate(source.splitlines()):
        line_num = i + 1
        for tag in ["{{", "{%", "}}", "%}"]:
            assert tag not in line, f"Jinja tag found, line {line_num}:\n\n{line}\n"


def confirm_other_schools_not_included(source: str, school_id: str):
    school_text = SCHOOL_TEXT[school_id]
    for i, line in enumerate(source.splitlines()):
        line_num = i + 1
        check_line(line, line_num, school_text)


def render_cell(cell: NotebookNode, school_id: str):
    cell.source = render_template(cell.source, school_id)

    confirm_no_jinja_tags(cell.source)
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

    def preprocess_cell(self, cell: NotebookNode, resources, index):
        if not self.school_id:
            raise RuntimeError(f"{type(self).__name__}.school_id must be set")

        cell = render_cell(cell, self.school_id)
        return cell, resources
