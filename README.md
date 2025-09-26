# Diff-based mutation testing GitHub Action

Write details

### Integration instructions

To use this action in your project you can use the following GitHub actions 
workflow template:

```
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

```
python3 main.py <path-to-diff-file> 
```

Run script

```
./run_all_patches.sh <patches-dir> <worktree-dir> <pytest_command> <output-file>
```

e.g.
```
./run_all_patches.sh patches worktree "pytest -q" results.txt
```
