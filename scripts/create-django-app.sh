#!/usr/bin/env bash

source "./set-public-env.sh";

cd "${PROJECT_ROOT_DIR}" || {
  printf "%s\n" "Unable to find project root dir. Bailing out now...";
  exit 1;
}

declare manage;

manage=$(find "${PROJECT_ROOT_DIR}" -name "manage.py");

if [[ $(command -v python) ]] ; then
  python "${manage}" "${1}";
  return 0;
else
  printf "%s\n" "Unable to locate python executable. Double check that python is installed and included in the system path.";
  exit 2;
fi;