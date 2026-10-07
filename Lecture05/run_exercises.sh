#!/bin/bash

show_comments="no"
questions=()
question_dir="/home/s1306053/BPSM/exercises/Lecture05"

# "$@" is all the arguments declared when running this file
for arg in "$@"
do
    if [[ "${arg}" == "-c" ]]
    then
        show_comments="yes"
    else
        # % removes .sh if declared in the argument so q1 or q1.sh works
	# add all the questions to an array 
        questions+=("${arg%.sh}")
    fi
done
 
# no questions named so run them all -eq checks equal to
if [[ ${#questions[@]} -eq 0 ]]
then
    questions=(q1 q2 q3 q4 q5 q6)
fi
 
for q in "${questions[@]}"
do
    script="${question_dir}/${q}.sh"

    # show the code
    printf "\n\n%s - code\n\n" "${script}"
    if [[ "${show_comments}" == "yes" ]]
    then
        cat "${script}"
    else
	# grep -v to remove comments i.e. minus visible
	# [[:space:]] * # to remove lines with any number of spaces at the start (because of ^) 
        tail -n +2 "${script}" | grep -v '^[[:space:]]*#' | cat
    fi
 
    # run the code
    printf "\n\n%s - output\n\n" "${script}"
    bash "${script}"
 
    echo
    echo
done





