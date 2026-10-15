#!/bin/bash

# Previews the site locally for one or both schools, without touching the current working tree. Each school is rendered in its own Git worktree under tmp/preview/, using the current working tree (including uncommitted and untracked changes), then copied to tmp/preview/<school>-site/ to be served by Jupyter Book's development server. Changes to the working tree are re-rendered and copied over, which reloads the open pages. (Copying means the server only ever sees fully-rendered files.)
#
# Usage:
#
#   ./extras/scripts/preview.sh [columbia] [nyu]
#
# Defaults to both schools. Ports default to 8101 (Columbia) and 8102 (NYU); override with COLUMBIA_PORT / NYU_PORT, or PORT when previewing one school. Each school's content server uses its port plus 100.
#
# Set PREVIEW_NO_SERVE=1 to instead do a one-off static build, exactly like CI, into tmp/preview/<school>/_build/html.

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

mkdir -p tmp/preview

# use a dedicated environment that matches the lockfile (like CI), leaving .venv alone
PREVIEW_VENV="$SRC/tmp/preview/.venv"
UV_PROJECT_ENVIRONMENT=$PREVIEW_VENV uv sync --locked --quiet
export PATH="$PREVIEW_VENV/bin:$PATH"

# snapshot the working tree (tracked + untracked, minus ignored) without touching the real index. The snapshot's index is kept between calls so that only changed files get re-hashed.
SNAPSHOT_INDEX="$SRC/tmp/preview/index"
cp "$(git rev-parse --git-path index)" "$SNAPSHOT_INDEX"
snapshot() {
    GIT_INDEX_FILE=$SNAPSHOT_INDEX git add -A
    GIT_INDEX_FILE=$SNAPSHOT_INDEX git write-tree
}

worktree() {
    echo "$SRC/tmp/preview/$1"
}

log() {
    echo "$SRC/tmp/preview/$1.log"
}

# copy the rendered files to where they're served, replacing each atomically, and only if changed
publish() {
    local school=$1
    rsync --archive --checksum --delete \
        --exclude=/.git --exclude=/_build \
        "$(worktree "$school")/" "$(worktree "$school")-site/"
}

# discard any previous render and turn the given tree into the school's version
prepare() {
    local tree=$1
    local school=$2
    local dir
    dir=$(worktree "$school")

    if [ ! -e "$dir/.git" ]; then
        git worktree add --detach "$dir" HEAD
    fi

    # commit the snapshot (unreferenced), like CI's preliminary commit, so the scripts can `git rm` cleanly
    local commit
    commit=$(git commit-tree "$tree" -p HEAD -m "preview snapshot")

    (
        cd "$dir"
        git checkout --detach --force --quiet "$commit"
        git clean -fdq
        if [ -n "$PREVIEW_NO_SERVE" ]; then
            ./extras/scripts/school_ci.sh "$school"
        else
            ./extras/scripts/school.sh "$school"
            publish "$school"
        fi
    ) >"$(log "$school")" 2>&1 ||
        {
            echo "$school build failed; see $(log "$school")" >&2
            return 1
        }
}

# re-render the files that changed between two snapshots
update() {
    local old=$1
    local new=$2
    local school=$3
    local dir
    dir=$(worktree "$school")

    (
        cd "$dir"
        # read line by line rather than with mapfile, which macOS's bash 3.2 lacks
        local changed=() deleted=() file
        while IFS= read -r file; do
            changed+=("$file")
        done < <(git diff --name-only --no-renames --diff-filter=d "$old" "$new")
        while IFS= read -r file; do
            deleted+=("$file")
        done < <(git diff --name-only --no-renames --diff-filter=D "$old" "$new")

        if [ ${#deleted[@]} -gt 0 ]; then
            git rm -q -f --ignore-unmatch -- "${deleted[@]}"
        fi
        if [ ${#changed[@]} -gt 0 ]; then
            git checkout "$new" -- "${changed[@]}"
            ./extras/scripts/school.sh "$school" "${changed[@]}"
        fi
        publish "$school"
    ) >>"$(log "$school")" 2>&1 ||
        echo "$school failed to update; see $(log "$school")" >&2
}

port_for() {
    # PORT (e.g. set by Claude's preview pane) applies when previewing a single school
    if [ -n "$PORT" ] && [ "$(echo "$SCHOOLS" | wc -w)" -eq 1 ]; then
        echo "$PORT"
        return
    fi
    case $1 in
        columbia) echo "${COLUMBIA_PORT:-8101}" ;;
        nyu) echo "${NYU_PORT:-8102}" ;;
    esac
}

TREE=$(snapshot)

# run the given function for each school in parallel, failing if any of them do
each_school() {
    local pids=() status=0
    for school in $SCHOOLS; do
        "$@" "$school" &
        pids+=($!)
    done
    # wait on these specifically, since the servers are also background jobs
    for pid in "${pids[@]}"; do
        wait "$pid" || status=1
    done
    return $status
}

each_school prepare "$TREE"

if [ -n "$PREVIEW_NO_SERVE" ]; then
    for school in $SCHOOLS; do
        echo "$school built: $(worktree "$school")/_build/html"
    done
    exit 0
fi

trap 'kill 0' EXIT
for school in $SCHOOLS; do
    port=$(port_for "$school")
    (
        cd "$(worktree "$school")-site"
        jupyter-book start --port "$port" --server-port $((port + 100)) >>"$(log "$school")" 2>&1 ||
            echo "$school server stopped; see $(log "$school")" >&2
    ) &
    echo "Serving $school at http://localhost:$port/"
done

echo "Watching for changes..."
while sleep 1; do
    tree=$(snapshot)
    if [ "$tree" = "$TREE" ]; then
        continue
    fi

    git diff --name-only --no-renames "$TREE" "$tree" | sed 's/^/Changed: /'
    if git diff --quiet "$TREE" "$tree" -- extras/lib/; then
        each_school update "$TREE" "$tree" || true
    else
        # the rendering itself changed, so start over
        each_school prepare "$tree" || true
    fi
    TREE=$tree
done
