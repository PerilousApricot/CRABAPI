#!/bin/bash
SCRIPTPATH="${BASH_SOURCE[0]}"                                                     
SCRIPT_BASE="$(cd "$(dirname $(dirname "${SCRIPTPATH}"))" ; pwd)" 
if [ ! -e ${SCRIPT_BASE}/.git/hooks/commit-msg ]; then
    ln -s ../../bin/git-commit-msg.sh ${SCRIPT_BASE}/.git/hooks/commit-msg
fi

if [ ! -e ${SCRIPT_BASE}/.git/hooks/pre-commit ]; then
    ln -s ../../bin/git-pre-commit.sh ${SCRIPT_BASE}/.git/hooks/pre-commit
fi

pylint --rcfile=pylintrc \
            --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" \
            --ignore=test_Task.py \
            -r n CRABAPI
if [ $? -eq 0 ]; then
    nosetests CRABAPI/ --cover-min-percentage=100 --with-coverage --cover-erase --cover-package=CRABAPI --cover-branches
fi
