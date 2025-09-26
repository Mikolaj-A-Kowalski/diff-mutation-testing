#!/bin/bash 

set -x

pwd

whoami

ls -al
ls -al /github/workspace

ls -al /app

git config --add safe.directory $(pwd)

git status 
git branch -a

git diff origin/master..HEAD
