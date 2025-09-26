#!/bin/bash 

#set -x

echo $@

# Get the user provided inputs
BUILD_COMMANDS=$1
TEST_COMMANDS=$2

# Make sure the build and test commands are provided
if [ -z "$BUILD_COMMANDS" ] || [ -z "$TEST_COMMANDS" ]
then
  echo "Error: Both build-commands and test-commands inputs are required."
  echo "Received build-commands: '$BUILD_COMMANDS'"
  echo "Received test-commands: '$TEST_COMMANDS'"
  exit 1
fi

# Make and activate Python venv
python -m venv venv
source venv/bin/activate

# Execute the build commands
echo "Executing build commands: $BUILD_COMMANDS"
eval "$BUILD_COMMANDS"


# Generate the diff
git diff origin/master..HEAD -- '*.py' > diff

echo "Generated diff:"
cat diff


# Run the scripts
python3 /app/main.py ./diff

for f in ./patches/*.diff; do
  echo "Patch file: $f"
  cat $f
done

/app/run_all_patches.sh ./patches worktree "${TEST_COMMANDS}" output.txt

cat output.txt

# ls -al
# ls -al /github/workspace

# ls -al /app

# git config --add safe.directory $(pwd)

# git status 
# git branch -a


