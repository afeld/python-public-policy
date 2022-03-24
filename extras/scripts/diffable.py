from nbconvert.preprocessors import Preprocessor


def has_html(output):
    return "text/html" in output.get("data", {})


# based off of
# https://github.com/jupyter/nbconvert/blob/master/nbconvert/preprocessors/tagremove.py
class Diffable(Preprocessor):
    def preprocess_cell(self, cell, resources, cell_index):
        if cell["cell_type"] != "code":
            return cell, resources

        # ignore any system command output, since things like package paths shown in warnings/errors can change between different systems
        if cell["source"][0].startswith("!"):
            cell["outputs"] = []

        # filter out warnings
        cell["outputs"] = [
            output for output in cell["outputs"] if output.get("name", None) != "stderr"
        ]

        if any(has_html(output) for output in cell["outputs"]):
            # clear HTML output, since it often has generated IDs (from displacy, plotly, etc.) that change with each execution
            cell["outputs"] = []

        return cell, resources
