# Corresponds to the Requirements for homework 5. Requires cloc and nbconvert. Usage:
#
#   python3 -m extras.scripts.hw_5_check <assignment>.ipynb

import ast
import json
import os
import pandas as pd
import re
import shlex
import subprocess
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ..lib.nb_helper import read_notebook, notebook_to_script

MIN_LINES = 40
VIZ_PACKAGES = set(
    [
        "altair",
        "bokeh",
        "folium",
        "geoplotlib",
        "geoviews",
        "ipyleaflet",
        "keplergl",
        "matplotlib",
        "plotly",
        "plotly.express",
        "plotnine",
        "pygal",
        "seaborn",
    ]
)

# https://sadh.life/post/ast/
class ImportsChecker(ast.NodeVisitor):
    def __init__(self):
        self.packages = set()

    def visit_Import(self, node):
        for name in node.names:
            self.packages.add(name.name)


class MethodChecker(ast.NodeVisitor):
    def __init__(self, method):
        self.method = method
        self.is_present = False

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute) and (
            node.func.attr == self.method
            or (isinstance(node.func.value, ast.Attribute) and node.func.value.attr == self.method)
        ):
            self.is_present = True


def handle_process_err(cmd, err):
    if type(cmd) == list:
        cmd = shlex.join(cmd)

    output = err.stderr.decode("utf-8")
    print(
        f"{bcolors.FAIL}ERROR{bcolors.ENDC} while running\n\n\t{cmd}\n\n{output}",
        file=sys.stderr,
    )
    sys.exit(err.returncode)


def get_cmd_output(cmd, input=None, shell=False):
    try:
        process = subprocess.run(
            cmd,
            capture_output=True,
            check=True,
            input=bytes(input, "utf-8"),
            shell=shell,
        )
    except subprocess.CalledProcessError as err:
        handle_process_err(cmd, err)

    return process.stdout


def lines_of_code(code):
    output = get_cmd_output("cloc --stdin-name=script.py --json -", input=code, shell=True)
    data = json.loads(output)
    return data["SUM"]["code"]


def code_contains(pattern, code):
    matches = re.search(re.compile(pattern, re.VERBOSE), code)
    return bool(matches)


def has_link(cell):
    pattern = r"https?://"
    if cell.cell_type == "code":
        # check for URL in comment
        pattern = r"^\s*\#.*" + pattern

    return code_contains(pattern, cell.source)


def includes_link(cells):
    return any(has_link(cell) for cell in cells)


def uses_transform(script):
    return code_contains(
        r"""\b(
               concat|
               groupby|
               join|
               melt|
               merge|
               pivot(_table)?|
               resample|
               (un)?stack
            )\(""",
        script,
    )


def has_overlap(set1, set2):
    return not set1.isdisjoint(set2)


def has_plotting(script):
    tree = ast.parse(script)

    imports_checker = ImportsChecker()
    imports_checker.visit(tree)

    method_checker = MethodChecker("plot")
    method_checker.visit(tree)

    return has_overlap(VIZ_PACKAGES, imports_checker.packages) or method_checker.is_present


# https://stackoverflow.com/a/287944/358804
class bcolors:
    OKGREEN = "\033[92m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


def pass_fail(result):
    """Apply ANSI color escape codes"""
    color = bcolors.OKGREEN if result else bcolors.FAIL
    return f"{color}{result}{bcolors.ENDC}"


def exit(results):
    exit_code = 0 if results.all() else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    notebook_path = sys.argv[1]

    notebook = read_notebook(notebook_path)
    script = notebook_to_script(notebook)
    num_lines = lines_of_code(script)

    # use pandas for outputting a table
    results = pd.Series(
        {
            f"Enough lines of code ({num_lines})": num_lines >= MIN_LINES,
            "Includes link": includes_link(notebook.cells),
            "Uses transform": uses_transform(script),
            "Has plotting": has_plotting(script),
        }
    )

    outputs = results.apply(lambda val: pass_fail(val))
    print(outputs.to_string())
    exit(results)
