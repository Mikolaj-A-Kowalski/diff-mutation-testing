# Diff-based mutation testing GitHub Action

This repository was created as part of the X-VISS hackathon 2025 by the following participants:
- Mikolaj Kowalski @Mikolaj-A-Kowalski
- Jack Franklin @jackdfranklin
- Matt Archer @ma595
- Sam Avis @sjavis

## Project overview
This Github action performs basic mutation testing on python code. Mutantions are generated only on modified code (using git diffs) to avoid an excessive number of mutants, so that it can be used as part of a CI workflow.

## Integration instructions

To use this action in your project you can use the following GitHub actions 
workflow template:

```yaml
name: mutation-testing

on:
  pull_request:
    types: [opened]

jobs:
  mutation:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Try the mutation testing
        uses: Mikolaj-A-Kowalski/diff-mutation-testing@master
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```



### Local execution

First generate a diff file:
```bash
git diff > <path-to-diff-file>
```

Then generate a set of mutation patch files using:
```bash
python3 main.py <path-to-diff-file> 
```

Finally, run the following script to perform the mutation testing:
```bash
./run_all_patches.sh <patches-dir> <worktree-dir> <pytest_command> <output-file>
```

e.g.
```bash
./run_all_patches.sh patches worktree "pytest -q" results.txt
```

The `results.txt` file includes a list of mutation patches that 'survived' - in other words mutations that the testing did not catch.
