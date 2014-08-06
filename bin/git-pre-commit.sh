#!/bin/bash
SCRIPTPATH="${BASH_SOURCE[0]}"                                                     
SCRIPT_BASE="$(cd "$(dirname $(dirname "${SCRIPTPATH}"))" ; pwd)" 

exec ${SCRIPT_BASE}/../bin/check-commit.sh
