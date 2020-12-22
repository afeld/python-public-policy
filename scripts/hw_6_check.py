# requires cloc

import json
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


notebook = sys.argv[1]
script = get_script(notebook)
num_lines = lines_of_code(script)
print("Lines of code:", num_lines)
