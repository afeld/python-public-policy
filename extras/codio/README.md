# Codio

## Creating the stack

Expanding on the [official instructions](https://docs.codio.com/develop/develop/stacks/create-stack.html):

1. [Create a `New Project` from this repository.](https://docs.codio.com/common/develop/ide/editing/git.html#manually-import-a-git-repo-into-codio)
   - Select the `jupyter-nbgrader` stack as the base.
1. [Open a Terminal.](https://docs.codio.com/common/develop/ide/boxes/terminal.html)
1. Run the setup.

   ```sh
   ./extras/codio/setup.sh
   ```

1. [Turn off `Protect Dynamic Ports`.](https://docs.codio.com/develop/develop/projects/project-settings.html)

## Creating Assignments

1. Switch to the `columbia` branch.
1. Create the assignment ZIP file.

   ```sh
   python extras/codio/hwzip.py hw_<num>
   ```

1. Create on the Codio side.

   1. Click `Add project-based assignment`.
   1. `Import`
   1. Use stack `python-public-policy`
   1. `Source`: `Zip File`
   1. Create the Guide.
      1. Paste in `This file can be ignored.`
      1. Under `Layout`:
         1. Select `Layout`: `1 Panel`.
         1. `Show file tree` should be off.

1. [Create on the Canvas side.](https://docs.codio.com/instructors/admin/integration/lms-systems/canvas.html#mapping-an-assignment-to-a-canvas-assignment)
