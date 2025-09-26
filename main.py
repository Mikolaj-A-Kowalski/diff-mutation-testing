# main.py
from mutate import mutate_candidates
from parse import parse_diff
from patch import produce_patch

import os
import sys
from typing import List, Tuple

Mutation = Tuple[str, int, str, str]


def generate_patches(patches_dir: str, mutations: List[Mutation]) -> None:
    """
    Generate patch files for each mutation in the list.

    Args:
        patches_dir: directory to save patch files.
        mutations: list of (file, line_number, old_line, new_line)
    """
    os.makedirs(patches_dir, exist_ok=True)

    print(mutations)

    for i, mutation in enumerate(mutations, start=1):
        patch_name = f"mutation_{i}.diff"
        patch_path = os.path.join(patches_dir, patch_name)
        produce_patch(mutation, patch_path)
        print(f"Wrote patch {patch_path}") 


def run(diff: str):
    """
    Run the mutation pipeline on a diffs file.

    Creates a series of patch files in the patches directory.

    Args:
        diff: Content of entire commit diff across all files

    Returns:
        None
    """

    # 1. Parse diff file into candidate tuples
    with open(diff, "r") as f:
        candidates = parse_diff(f)
    
    # 2. Run mutations
    mutations = mutate_candidates(candidates)

    # 3. Create a single patch
    # Create patch directory - use absolute path for safety.
    # TODO: check if this is needed.

    # project_root = os.path.dirname(__file__)  
    # patches_dir = os.path.join(project_root, "patches")
    patches_dir = "./patches"
    os.makedirs(patches_dir, exist_ok=True)

    generate_patches(patches_dir, mutations)


def main():
    if len(sys.argv) != 2:
       print("Usage: python main.py <diffs-file>")
       sys.exit(1)

    diff = sys.argv[1]

    run(diff)


if __name__ == "__main__":
    main()
