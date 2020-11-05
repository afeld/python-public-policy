import json
import re
import sys


def is_pip_upgrade_msg(line):
    return isinstance(line, str) and re.match(r"WARNING.+pip version|upgrade pip", line)


def is_vid(cell):
    try:
        text = cell["outputs"][0]["data"]["text/plain"][0]
    except (IndexError, KeyError, TypeError):
        return False

    return text == "<IPython.core.display.Video object>"


input_str = sys.stdin.read()
notebook = json.loads(input_str)

# nbconvert wants to embed videos, so skip them
notebook["cells"] = [cell for cell in notebook["cells"] if not is_vid(cell)]

for cell in notebook["cells"]:
    if "execution_count" in cell:
        # ignore all the execution count numbers
        cell["execution_count"] = None

    if cell["cell_type"] != "code":
        continue

    # ignore any system command output
    if cell["source"][0].startswith("!"):
        cell["outputs"] = []

    # filter out pip upgrade warnings
    cell["outputs"] = [line for line in cell["outputs"] if not is_pip_upgrade_msg(line)]

    for output in cell["outputs"]:
        if "execution_count" in output:
            # ignore all the execution count numbers
            output["execution_count"] = 1

        # clear HTML output, since it often has generated IDs (from displacy, plotly, etc.) that change with each execution
        if "data" in output and "text/html" in output["data"]:
            cell["outputs"] = []
            # go to next cell
            break


print(json.dumps(notebook, indent=2, sort_keys=True))
