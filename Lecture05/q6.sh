#!/bin/bash

#Using an array to process the Mozambique data

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"

mozambique_names=()

while IFS=$'\t' read -r name email city day month year country
do
    if [[ "${name}" != "name" && "${name}" != "" ]]
    then
        if [[ "${country}" == "Mozambique" ]]
        then
            mozambique_names+=("${name}")
        fi
    fi
done < "${data_file}"

printf 'Number of people from Mozambique: %s\n\n' "${#mozambique_names[@]}"

counter=0

for person in "${mozambique_names[@]}"
do
    counter=$((counter + 1))
    printf '%s: %s\n' "${counter}" "${person}"
done






