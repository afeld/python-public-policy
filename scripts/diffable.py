import re
from nbconvert.preprocessors import Preprocessor


def is_pip_upgrade_msg(line):
    return isinstance(line, str) and re.match(r"WARNING.+pip version|upgrade pip", line)


def remove_path(output):
    """Paths differ on different systems, so cut them out"""
    if output["output_type"] == "stream" and output["name"] == "stderr":
        output["text"] = [
            re.sub(r"/usr/.*/python.*\.py:\d+:", "", line) for line in output["text"]
        ]
    return output


def has_html_output(output):
    return "data" in output and "text/html" in output["data"]


# based off of
# https://github.com/jupyter/nbconvert/blob/master/nbconvert/preprocessors/tagremove.py
class Diffable(Preprocessor):
    def preprocess_cell(self, cell, resources, cell_index):
        if cell["cell_type"] != "code":
            return cell, resources

        # ignore any system command output
        if cell["source"][0].startswith("!"):
            cell["outputs"] = []

        # filter out pip upgrade warnings and clean up paths
        cell["outputs"] = [
            remove_path(line)
            for line in cell["outputs"]
            if not is_pip_upgrade_msg(line)
        ]

        for output in cell["outputs"]:
            if has_html_output(output):
                # clear HTML output, since it often has generated IDs (from displacy, plotly, etc.) that change with each execution
                cell["outputs"] = []
                # go to next cell
                break

        return cell, resources
