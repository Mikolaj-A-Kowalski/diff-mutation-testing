# main.py
import os
from parse import parse_diff   
from mutate import mutate_candidates
import sys


def generate_patches(mutations):
    pass
   

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

    project_root = os.path.dirname(__file__)  
    patches_dir = os.path.join(project_root, "patches")
    os.makedirs(patches_dir, exist_ok=True)

    generate_patches(mutations[0])



def main():
    if len(sys.argv) != 2:
       print("Usage: python main.py <diffs-file>")
       sys.exit(1)

    diff = sys.argv[1]

    run(diff)


if __name__ == "__main__":
    main()
