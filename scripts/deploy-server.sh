#!/usr/bin/env bash

source "./set-public-env.sh";

declare CWDir;
declare ExitCount;

CWDir=$(pwd);
ExitCount=0;

ExitCount++;
cd "${Project_Root_Dir}" || {
  printf "%s\n" "Bad trouble in 'cd ${Project_Root_Dir}'. Bailing out...";
  exit $ExitCount;
}

# Verify that we can find the python executable before calling it:
ExitCount++;
if [[ $(command -v python) ]] ; then
  python "${Django_Manager}" "check" --deploy;
else
  printf "%s\n" "Could not find python executable. Bailing out...";
  exit $ExitCount;
fi;

# Restore the original working directory
ExitCount++;
cd "${CWDir}" || {
  printf "%s\n" "Bad trouble in 'cd ${CWDir}'. Bailing out...";
  exit $ExitCount;
}