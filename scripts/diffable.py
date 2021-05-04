from nbconvert.preprocessors import Preprocessor


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

        # filter out warnings
        cell["outputs"] = [
            output for output in cell["outputs"] if output.get("name", None) != "stderr"
        ]

        for output in cell["outputs"]:
            if has_html_output(output):
                # clear HTML output, since it often has generated IDs (from displacy, plotly, etc.) that change with each execution
                cell["outputs"] = []
                # go to next cell
                break

        return cell, resources
