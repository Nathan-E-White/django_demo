#!/usr/bin/env bash

source "../set-public-env.sh";

cd "${PROJECT_ROOT_DIRECTORY}" || {
  printf "%s\n" "Unable to cd to project root directory. Bailing out now...";
  exit 1;
}

declare mb;
declare lb;
declare nb;

mb="${PROJECT_MAIN_BRANCH}";
nb=${#PROJECT_OTHER_BRANCHES[@]};

if [[ $nb -gt 0 ]] ; then
  for i in "${PROJECT_OTHER_BRANCHES[@]}" ; do
    lb="${i}|${lb}"
  done
fi;

### Git branch --merged:
# lists branches currently merged with your current checked out branch.

### grep -Ev "(^\*|master|dev)":
# invert matching with grep, excludes branches to keep

### xargs git branch -d:
# deletes every branch passed in to the command.
git branch --merged | grep -Ev "(^\*|${mb}|${lb})" | xargs git branch -d;

exit 0;
