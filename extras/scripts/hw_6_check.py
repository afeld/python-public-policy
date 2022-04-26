# Helper file for homework 6. The checks correspond to the Requirements for homework 6. Requires cloc and nbconvert.

import ast
import json
import re
import shlex
import subprocess
import sys


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
            or (
                isinstance(node.func.value, ast.Attribute)
                and node.func.value.attr == self.method
            )
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
    output = get_cmd_output(
        "cloc --stdin-name=script.py --json -", input=code, shell=True
    )
    data = json.loads(output)
    return data["SUM"]["code"]


def code_contains(pattern, code):
    matches = re.search(re.compile(pattern, re.VERBOSE), code)
    return bool(matches)


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

    return (
        has_overlap(VIZ_PACKAGES, imports_checker.packages) or method_checker.is_present
    )


# https://stackoverflow.com/a/287944/358804
class bcolors:
    FAIL = "\033[91m"
    ENDC = "\033[0m"
