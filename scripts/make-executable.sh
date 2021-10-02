#!/usr/bin/env bash

source "./set-public-env.sh";

function make-executable {

  if [[ $# -eq 0x0 ]] ; then
    printf "%s\n" "$0 called with zero arguments, exiting.";
    exit 1;
  fi;

  # See SC2185; some systems don't have a default path to search
  path=$(find "${PROJECT_ROOT_DIRECTORY}" "${1}");

  # Set the file to be executable; note, relying on user to sudo themselves when calling the command.
  chmod a+x "${path}";
  exit 0;
}