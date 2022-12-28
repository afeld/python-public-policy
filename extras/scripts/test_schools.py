import pytest

COURSE_HOSTNAME = "python-public-policy.afeld.me"
NYU_WORDS = [
    "brightspace",
    "conversation",  # Brightspace term
    "jupyterhub",
    "nyu",
    "padm",
    "python coding for public policy",  # Columbia version doesn't include "Coding"
    "wagner",
]
EXEMPT = ["hannahkates/nyu-python-public-policy"]


def check_line(file, line, line_num):
    for word in NYU_WORDS:
        for exemption in EXEMPT:
            if exemption in line.lower():
                return

        msg = f'"{word}" found in {file}, line {line_num}:\n\n{line}'
        assert word not in line.lower(), msg

    # site checks

    msg = f"Linking to NYU course site in {file}, line {line_num}:\n\n{line}"

    for path in ["/latest", "/nyu"]:
        assert f"{COURSE_HOSTNAME}/en{path}" not in line, msg

    if COURSE_HOSTNAME in line:
        # (imperfectly) assure it's linking to the Columbia version
        assert f"{COURSE_HOSTNAME}/en/columbia" in line, msg


@pytest.mark.parametrize("file", ["syllabus.md", "README.md"])
def test_syllabus_no_nyu(file):
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            line_num = i + 1
            check_line(file, line, line_num)
