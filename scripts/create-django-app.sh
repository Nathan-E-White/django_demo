#!/usr/bin/env bash

source "./set-public-env.sh";
declare CWDir;
declare ExitCount

CWDir=$(pwd);
ExitCount=0

ExitCount++;
cd "${PROJECT_ROOT_DIR}" || {
  printf "%s\n" "Unable to find project root directory: ${PROJECT_ROOT_DIR}. Bailing out now...";
  exit $ExitCount;
}

ExitCount++;
if [[ $(command -v python) ]] ; then
  # shellcheck disable=SC2154
  python "${Django_Manager}" "${1}";
else
  printf "%s\n" "Unable to locate python executable. Double check that python is installed and included in the system path.";
  exit $ExitCount;
fi;

ExitCount++;
cd "${CWDir}" || {
  printf "%s\n" "Unable to cd into previous working directory: ${CWDir}. Bailing out...";
  exit $ExitCount;
}

exit 0;