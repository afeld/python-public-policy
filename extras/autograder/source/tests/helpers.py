import ast
from typing import Union


def base_obj(node: ast.Call) -> Union[str, None]:
    """If this is a method call, return the name of the base object it was called on"""
    if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
        return node.func.value.id
    else:
        return None


class PlotChecker(ast.NodeVisitor):
    def visit_Call(self, node):
        if base_obj(node) == "px":
            args = [kw.arg for kw in node.keywords]
            method = node.func.attr

            if method == "get_trendline_results":
                # `title` not applicable
                return

            assert "title" in args, f"call to `{method}()` missing a `title`"


def check_plots(source: str):
    tree = ast.parse(source)
    checker = PlotChecker()
    checker.visit(tree)
