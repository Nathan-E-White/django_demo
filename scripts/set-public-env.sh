#!/usr/bin/env bash

## Declare project globals; intentional use of upper camel case
# declare -export Project_Root_Dir;
# declare -export Project_Main_Branch;
# declare -ae Project_Other_Branches;
# declare -export Django_Manager;

## Declare local variables for this script
CWDir=.;
PRDTarget=.;
PRDValidated=.;
ExitCall=0;
MTarget=.;
MValidated=.;

# Set main project root directory
PRDTarget="/mnt/d/Software-Development/pyAppProj/analytics/";

# Set the main repository used by Git
Project_Main_Branch="master";

# Set the name of the Django manager file
MTarget="manager.py";

# Uncomment for adding other branches for Git; i.e. branches for each developer, branches for a single day/project, etc.
# Project_Other_Branches[0]="Developers";
# Project_Other_Branches[1]="SprintNNN";

# Get the current working directory from the shell
CWDir=$(pwd);

# Verify that we can find the directory listed as the source root
PRDValidated=$(find "${PRDTarget}");

# TODO: could create the project root if it doesn't exist and create the Django project automatically. Right now PyCharm is doing the heavy lifting on that end.
if [[ ! -d "${PRDValidated}" ]] ; then
  printf "%s\n" "Could not find project root directory. Please check that it exists and try again.";
  exit $ExitCall;
fi;

# Assume that if the script made it through the previous if statement then the project root is good to go.
Project_Root_Dir="${PRDValidated}";

# cd into the project root
cd "${Project_Root_Dir}" || {
  printf "%s\n" "Bad trouble in 'cd ${Project_Root_Dir}', bailing out now.";
  exit $ExitCall;
}

# Verify the manage.py file exists
MValidated=$(find "${Project_Root_Dir}" -f "${Project_Root_Dir}\\${MTarget}");

# Validate the manage.py file
if [[ ! -f "${MValidated}" ]] ; then
  printf "%s\n" "Could not find manage.py file in ${Project_Root_Dir}. Bailing out...";
  exit $ExitCall;
fi;

if [[ ! -s "${MValidated}" ]] ; then
  printf "%s\n" "Found manage.py file in ${Project_Root_Dir}, but it appears to be empty to the shell. Check that it was installed correctly. Bailing out...";
  exit $ExitCall;
fi;

Django_Manager="${MValidated}";

## After processing, export the project constants
export Project_Root_Dir;
export Project_Main_Branch;
export Project_Other_Branches;
export Django_Manager;

# Change back to the directory the shell was in before the script was called
cd "${CWDir}" || {
  printf "%s\n" "Bad trouble in 'cd ${CWDir}'. Bailing out now...";
  exit $ExitCall;
}