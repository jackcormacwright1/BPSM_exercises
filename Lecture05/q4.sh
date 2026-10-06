#!/bin/bash

#Work out how many people were born in October, and where are they from, output the list of people

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"
output_file="./q4_october_births.txt"

printf 'Name\tCountry\n' > "${output_file}"

while IFS=$'\t' read -r name email city day month year country
do
        if [[ ${name} != "name" && ${name} != "" ]]
        then
                if [[ ${month} = 10 ]]
		then
			printf '%s\t%s\n' "${name}" "${country}" >> "${output_file}"
		fi
        fi

done < "${data_file}"

printf "October births saved to %s\n" "${output_file}"

printf "\nNumber of October births:\n\n"

tail -n +2 "${output_file}" | wc -l

echo

head -n 1 "${output_file}"
tail -n +2 "${output_file}" | sort -t $'\t' -k2,2 -k1,1

echo



