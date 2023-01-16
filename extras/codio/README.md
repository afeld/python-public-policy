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
   1. `Source`: `Zip File`, unloading the file from above
   1. Create
   1. Save the notebook so that the `Python 3` kernel is selected
   1. `Publish`

1. [Create on the Canvas side.](https://docs.codio.com/instructors/admin/integration/lms-systems/canvas.html#mapping-an-assignment-to-a-canvas-assignment)
