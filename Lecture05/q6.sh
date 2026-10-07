#!/bin/bash

#Using an array to process the Mozambique data

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"

# create the empty array for us to store the variables
# i am using it to count the number of people from mozambique
mozambique_names=()

while IFS=$'\t' read -r name email city day month year country
do
    if [[ "${name}" != "name" && "${name}" != "" ]]
    then
        if [[ "${country}" == "Mozambique" ]]
        then
	    # += to add a new value to the variable
	    # this is the same as doing array = array + ... and will append the assigned value to the end of the created list
	    # here we add the name from the data file if the country is mozambique
	    # quotes mean if there are spaces in the name it will still be read as one value
	    # brackets are needed to tell bash this is a list element
	    # otherwise it will try to join as text
            mozambique_names+=("${name}")
        fi
    fi

# input the data rather than piping because we want to access the array afterwards
# if the data were piped to the while loop it would run in a subshell and the array would be inaccessable
done < "${data_file}"

# square brackets after the array name say we want to access its contents,
# @ means all of them and # before the array name means count the items
printf 'Number of people from Mozambique: %s\n\n' "${#mozambique_names[@]}"

counter=0

# loop to output the names with an index
for person in "${mozambique_names[@]}"
do
    counter=$((counter + 1))
    printf '%s: %s\n' "${counter}" "${person}"
done






