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
    pattern = r"https?://"
    if cell["cell_type"] == "code":
        # check for URL in comment
        pattern = r"^\s*#.*" + pattern

    return any(re.match(pattern, line) for line in cell["source"])


def includes_link(notebook):
    return any(has_link(cell) for cell in notebook["cells"])


# https://stackoverflow.com/a/287944/358804
class bcolors:
    OKGREEN = "\033[92m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


def pass_fail(result):
    result = bool(result)
    color = bcolors.OKGREEN if result else bcolors.FAIL
    return f"{color}{result}{bcolors.ENDC}"


notebook_path = sys.argv[1]
script = get_script(notebook_path)

num_lines = lines_of_code(script)
print("Enough lines of code:", f"{pass_fail(num_lines >= 40)} ({num_lines})")

notebook = json.load(open(notebook_path))
print("Includes link:", pass_fail(includes_link(notebook)))

uses_transform = re.match(r"(groupby|merge|join|concat)\(", str(script))
print("Uses transform:", pass_fail(uses_transform))

has_plotting = re.match(r"(groupby|merge|join|concat)\(", str(script))
print("Has plotting:", pass_fail(has_plotting))
