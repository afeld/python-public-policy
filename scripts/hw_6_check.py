# requires cloc

import json
import pandas as pd
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

script_bytes = get_script(notebook_path)
script = str(script_bytes)
notebook = json.load(open(notebook_path))

num_lines = lines_of_code(script_bytes)
uses_transform = re.match(r"(groupby|merge|join|concat)\(", script)
has_plotting = re.match(r"plotly|matplotlib|altair", script)

# use pandas for outputting a table
series = pd.Series(
    {
        f"Enough lines of code ({num_lines})": num_lines >= 40,
        "Includes link": includes_link(notebook),
        "Uses transform": uses_transform,
        "Has plotting": has_plotting,
    }
)

series = series.apply(lambda val: pass_fail(val))
print(series.to_string())
