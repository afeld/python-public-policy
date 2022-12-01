NYU_WORDS = [
    "brightspace",
    "conversation",  # Brightspace term
    "jupyterhub",
    "nyu",
    "padm",
    "python coding for public policy",
    "wagner",
]


def test_syllabus_no_nyu():
    with open("syllabus.md") as f:
        for i, line in enumerate(f.readlines()):
            line_num = i + 1
            for word in NYU_WORDS:
                msg = f'"{word}" found in syllabus, line {line_num}:\n\n{line}'
                assert word not in line.lower(), msg
