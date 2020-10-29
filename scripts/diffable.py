import json
import re
import sys

def is_pip_upgrade_msg(line):
    return isinstance(line, str) and re.match(r"WARNING.+pip version|upgrade pip", line)

input_str = sys.stdin.read()
notebook = json.loads(input_str)

for cell in notebook["cells"]:
    if "execution_count" in cell:
        # ignore all the execution count numbers
        cell["execution_count"] = None

    if cell["cell_type"] != "code":
        continue

    # filter out pip upgrade warnings
    cell["outputs"] = [
        line
        for line in cell["outputs"]
        if not is_pip_upgrade_msg(line)
    ]

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
