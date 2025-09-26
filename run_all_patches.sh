#!/usr/bin/env bash
set -euo pipefail

# Usage: ./run_all_patches.sh <patches-dir> <worktree-dir> <test-command> <results-file>
# Example: ./run_all_patches.sh patches worktree "pytest -q" results.txt

PATCHES_DIR=$1
WORKTREE=$2
TEST_CMD=$3
RESULTS_FILE=$4

# clean results file
: > "$RESULTS_FILE"

for PATCH_FILE in "$PATCHES_DIR"/*.diff; do
    PATCH_NAME=$(basename "$PATCH_FILE")
    echo "Testing patch: $PATCH_NAME"

    PATCH_FILE=$(realpath "$PATCH_FILE")

    cat $PATCH_FILE

    # fresh worktree for each patch
    rm -rf "$WORKTREE"
    git worktree add "$WORKTREE" HEAD
    cd "$WORKTREE"

    if patch -p0 <$PATCH_FILE; then
        echo "Applied patch: $PATCH_NAME"
    else
        echo "Failed to apply patch: $PATCH_NAME"
        cd ..
        git worktree remove --force "$WORKTREE"
        continue
    fi

    echo "Running tests..."
    if bash -c "$TEST_CMD"; then
        echo "$PATCH_NAME Survived" >> "../$RESULTS_FILE"
    else
        echo "$PATCH_NAME Killed" >> "../$RESULTS_FILE"
    fi

    cd ..
    git worktree remove --force "$WORKTREE"
done

echo "Summary written to $RESULTS_FILE"

