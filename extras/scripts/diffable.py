from nbconvert.preprocessors import Preprocessor

def is_system_command(source):
    return source.startswith("!")

def is_ipytest(source):
    return source.startswith("%%ipytest")

def has_html(output):
    return "text/html" in output.get("data", {})

def has_html_output(cell):
    return any(has_html(output) for output in cell["outputs"])

def should_clear_output(cell):
    """Ignore any system command and ipytest output, since things like package paths shown in warnings/errors can change between different systems. Also clear HTML output, since it often has generated IDs (from displacy, plotly, etc.) that change with each execution."""
    source = cell["source"]
    return is_system_command(source) or is_ipytest(source) or has_html_output(cell)



# based off of
# https://github.com/jupyter/nbconvert/blob/master/nbconvert/preprocessors/tagremove.py
class Diffable(Preprocessor):
    def preprocess_cell(self, cell, resources, cell_index):
        if cell["cell_type"] != "code":
            return cell, resources

        if should_clear_output(cell):
            cell["outputs"] = []

        # filter out warnings
        cell["outputs"] = [
            output for output in cell["outputs"] if output.get("name", None) != "stderr"
        ]

        return cell, resources
