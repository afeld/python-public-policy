# requires cloc

import json
import re
import subprocess
import sys


def get_cmd_output(cmd, input=None, shell=False):
    process = subprocess.run(cmd, capture_output=True, input=input, shell=shell)
    return process.stdout


def get_script(notebook_path):
    return get_cmd_output(
        [
            "jupyter",
            "nbconvert",
            "--to",
            "script",
            "--log-level",
            "WARN",
            "--stdout",
            notebook_path,
        ]
    )


def lines_of_code(code):
    output = get_cmd_output(
        "cloc --stdin-name=script.py --json -", input=code, shell=True
    )
    data = json.loads(output)
    return data["SUM"]["code"]


def has_link(cell):
    if cell["cell_type"] == "code":
        # check for URL in comment
        pattern = "^\s*#.*https?://"
    else:
        pattern = "https?://"

    return any(re.match(pattern, line) for line in cell["source"])


def includes_link(notebook):
    return any(has_link(cell) for cell in notebook["cells"])


notebook_path = sys.argv[1]
script = get_script(notebook_path)

num_lines = lines_of_code(script)
print("Lines of code:", num_lines)

notebook = json.load(open(notebook_path))
print("Includes link:", includes_link(notebook))
