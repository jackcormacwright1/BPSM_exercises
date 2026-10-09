#!/bin/bash

#Work out how many people were born in October, and where are they from, output the list of people

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"
output_file="./q4_october_births.txt"

printf 'Name\tCountry\n' > "${output_file}"

counter=0

while IFS=$'\t' read -r name email city day month year country
do
        if [[ ${name} != "name" && ${name} != "" ]]
        then
	        # 10 for october so if it is not the header and not blank (above) AND month = 10 
		if [[ ${month} = 10 ]]
		then
			# >> to append to the file at the end not replace the file
			printf '%s\t%s\n' "${name}" "${country}" >> "${output_file}"
			counter=$((counter + 1))
		fi
        fi

done < "${data_file}"

printf "October births saved to %s\n" "${output_file}"

printf "\nNumber of October births:\n\n"
printf '%s\n' "${counter}"

echo

# IFS= means do not split the line so the whole line is read into the variable for printing
while IFS= read -r line
do
	printf '%s\n' "${line}"
done < "${output_file}"

echo



