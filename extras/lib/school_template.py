import dataclasses
import re
from pathlib import Path

from jinja2 import Environment, StrictUndefined
from nbconvert.preprocessors import Preprocessor
from nbformat import NotebookNode
from traitlets.traitlets import Unicode

from .school import EXEMPT, SCHOOL_TEXT, SCHOOLS, SchoolText

COURSE_HOSTNAME = "python-public-policy.afeld.me"
REPO_ROOT = Path(__file__).resolve().parents[2]
# Markdown links to other pages, e.g. [Syllabus](syllabus.md#schedule), but not ones with a scheme or that are only an anchor
RELATIVE_LINK = re.compile(
    r"(?<!!)\]\((?![a-z]+:|#)([^)#\s]+\.(?:md|ipynb))(#[^)\s]*)?\)"
)

env = Environment(
    undefined=StrictUndefined,
    autoescape=False,
)


def get_vars(school_id: str):
    school_text = SCHOOL_TEXT[school_id]
    return dataclasses.asdict(school_text)


def render_template(source: str, school_id: str):
    template = env.from_string(source)
    local_vars = get_vars(school_id)
    return template.render(**local_vars)


def page_url(target: str, nb_dir: Path, school_slug: str):
    """The absolute site URL for a page's source file, linked from a notebook in nb_dir."""

    path = (nb_dir / target).resolve()
    assert path.is_file(), f"Link target not found: {target}"

    # Jupyter Book 2 builds pages at slugs like assignments/open_ended.md -> assignments/open-ended/
    page = path.relative_to(REPO_ROOT).with_suffix("").as_posix()
    slug = "" if page == "index" else re.sub(r"[^a-z0-9/]+", "-", page.lower()) + "/"
    return f"https://{COURSE_HOSTNAME}/en/{school_slug}/{slug}"


def absolutize_links(source: str, nb_dir: Path, school_slug: str):
    """Rewrites relative links to pages so they work when the notebook is opened elsewhere, like Colab."""

    def replace(match: re.Match):
        url = page_url(match[1], nb_dir, school_slug)
        return f"]({url}{match[2] or ''})"

    return RELATIVE_LINK.sub(replace, source)


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


def render_cell(cell: NotebookNode, school_id: str, nb_dir: Path = REPO_ROOT):
    cell.source = render_template(cell.source, school_id)
    if cell.cell_type == "markdown":
        school_slug = SCHOOL_TEXT[school_id].school_slug
        cell.source = absolutize_links(cell.source, nb_dir, school_slug)

    confirm_no_jinja_tags(cell.source)
    confirm_other_schools_not_included(cell.source, school_id)

    return cell


# https://nbconvert.readthedocs.io/en/latest/nbconvert_library.html#Custom-Preprocessors
class SchoolTemplate(Preprocessor):
    school_id = Unicode().tag(config=True)

    def preprocess(self, nb, resources):
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

        # nbconvert sets the path to the notebook's directory, relative to the working directory
        nb_dir = Path(resources.get("metadata", {}).get("path", "")).resolve()
        cell = render_cell(cell, self.school_id, nb_dir)
        return cell, resources
