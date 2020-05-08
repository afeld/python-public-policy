import json
import re
import sys

input_str = sys.stdin.read()
notebook = json.loads(input_str)

for cell in notebook["cells"]:
    if "execution_count" in cell:
        # ignore all the execution count numbers
        cell["execution_count"] = None

    # filter out pip upgrade warnings
    cell["outputs"] = [
        line
        for line in cell["outputs"]
        if not re.match(r"WARNING: You are using pip version|--upgrade pip", line)
    ]

    if cell["cell_type"] != "code":
        continue

    for output in cell["outputs"]:
        # clear HTML output, since it often has generated IDs (from displacy, plotly, etc.) that change with each execution
        if "data" in output and "text/html" in output["data"]:
            cell["outputs"] = []
            # go to next cell
            break


print(json.dumps(notebook, indent=2, sort_keys=True))
