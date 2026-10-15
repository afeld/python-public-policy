#!/bin/bash

# Builds and serves the site locally for one or both schools, without touching the current working tree. Each school is rendered in its own Git worktree under tmp/preview/, using the current working tree (including uncommitted and untracked changes).
#
# Usage:
#
#   ./extras/scripts/preview.sh [columbia] [nyu]
#
# Defaults to both schools. Ports default to 8101 (Columbia) and 8102 (NYU); override with COLUMBIA_PORT / NYU_PORT, or PORT when previewing one school. Set PREVIEW_NO_SERVE=1 to only build.

set -e

SRC=$(git rev-parse --show-toplevel)
cd "$SRC"

SCHOOLS=${*:-columbia nyu}
for school in $SCHOOLS; do
    case $school in
        columbia | nyu) ;;
        *)
            echo "Unknown school: $school" >&2
            exit 1
            ;;
    esac
done

# use a dedicated environment that matches the lockfile (like CI), leaving .venv alone
PREVIEW_VENV="$SRC/tmp/preview/.venv"
UV_PROJECT_ENVIRONMENT=$PREVIEW_VENV uv sync --locked --quiet
export PATH="$PREVIEW_VENV/bin:$PATH"

# snapshot the working tree (tracked + untracked, minus ignored) without touching the real index
SNAPSHOT_INDEX=$(mktemp)
cp "$(git rev-parse --git-path index)" "$SNAPSHOT_INDEX"
GIT_INDEX_FILE=$SNAPSHOT_INDEX git add -A
TREE=$(GIT_INDEX_FILE=$SNAPSHOT_INDEX git write-tree)
rm -f "$SNAPSHOT_INDEX"
# commit it (unreferenced), like CI's preliminary commit, so school_ci.sh can `git rm` cleanly
SNAPSHOT=$(git commit-tree "$TREE" -p HEAD -m "preview snapshot")

port_for() {
    # PORT (e.g. set by Claude's preview pane) applies when previewing a single school
    if [ -n "$PORT" ] && [ "$(echo $SCHOOLS | wc -w)" -eq 1 ]; then
        echo "$PORT"
        return
    fi
    case $1 in
        columbia) echo "${COLUMBIA_PORT:-8101}" ;;
        nyu) echo "${NYU_PORT:-8102}" ;;
    esac
}

build() {
    local school=$1
    local dir="$SRC/tmp/preview/$school"

    if [ ! -e "$dir/.git" ]; then
        git worktree add --detach "$dir" "$SNAPSHOT"
    fi

    (
        cd "$dir"
        # match the snapshot exactly, discarding the previous render
        git checkout --detach --force --quiet "$SNAPSHOT"
        git clean -fdq
        ./extras/scripts/school_ci.sh "$school" >build.log 2>&1 ||
            {
                echo "$school build failed; see $dir/build.log" >&2
                exit 1
            }
    )
    echo "$school built: $dir/_build/html"
}

pids=()
for school in $SCHOOLS; do
    build "$school" &
    pids+=($!)
done
for pid in "${pids[@]}"; do
    wait "$pid"
done

if [ -n "$PREVIEW_NO_SERVE" ]; then
    exit 0
fi

trap 'kill 0' EXIT
for school in $SCHOOLS; do
    port=$(port_for "$school")
    echo "Serving $school at http://localhost:$port/"
    python -m http.server "$port" --bind 127.0.0.1 -d "$SRC/tmp/preview/$school/_build/html" >/dev/null 2>&1 &
done
wait
