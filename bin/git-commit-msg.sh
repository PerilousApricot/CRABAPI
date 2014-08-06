#!/bin/bash

# Try and force some sensible commit checking

FIRST_LINE=`grep -v '^#' $1 |head -n1`
SECOND_LINE=`grep -v '^#' $1 |head -n2 | tail -n1`

FIRST_LENGTH=${#FIRST_LINE}
SECOND_LENGTH=${#SECOND_LINE}
REMAINDER_LONGEST=$(grep -v '^#' $1 | tail -n +3 | awk 'length > max_length { max_length = length; longest_line = $0 } END { print longest_line }')
REMAINDER_LENGTH=${#REMAINDER_LONGEST}

if [[ $(grep -v '^#' $1 | wc -l) -eq 1 && $FIRST_LENGTH -lt 51 ]]; then
    exit 0
fi

if [[ $FIRST_LENGTH -gt 50 || $SECOND_LENGTH -gt 0 || $REMAINDER_LENGTH -gt 72 ]]; then
    echo "This commit message isn't formatted properly. The canonical explanation
of a 'good' commit message can be found here:

http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html

This script requires a 50-char summary line, followed by a blank link, followed
by a 72-char max body

If you're REALLY insistant on using the current commit message, you may execute
git commit --no-verify -F BAD-COMMIT-MSG.txt to retry the commit

These are the values I got: ($FIRST_LENGTH, $SECOND_LENGTH, $REMAINDER_LENGTH)"
    cp $1 BAD-COMMIT-MSG.txt
    exit 1
else
    exit 0
fi
