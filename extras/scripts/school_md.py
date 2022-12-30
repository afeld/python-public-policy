from argparse import ArgumentParser
from ..lib.school import render_template

parser = ArgumentParser(
    # https://stackoverflow.com/a/8789689/358804
    prog=f"python -m {__loader__.name}",
    description="Render template with school data.",
)
parser.add_argument("filename")
parser.add_argument("school_slug")
parser.add_argument("--inplace", action="store_true")

args = parser.parse_args()

mode = "r+" if args.inplace else "r"
with open(args.filename, mode) as f:
    source = f.read()

    result = render_template(source, args.school_slug)
    # Jinja2 seems to strip the trailing newline
    if not result.endswith("\n"):
        result += "\n"

    if args.inplace:
        f.seek(0)
        f.write(result)
        f.truncate()
    else:
        print(result)
