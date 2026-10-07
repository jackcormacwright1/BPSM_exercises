#!/bin/bash

#Work out how many people were born in October, and where are they from, output the list of people

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"
output_file="./q4_october_births.txt"

printf 'Name\tCountry\n' > "${output_file}"

while IFS=$'\t' read -r name email city day month year country
do
        if [[ ${name} != "name" && ${name} != "" ]]
        then
	        # 10 for october so if it is not the header and not blank (above) AND month = 10 
		if [[ ${month} = 10 ]]
		then
			# >> to append to the file at the end not replace the file
			printf '%s\t%s\n' "${name}" "${country}" >> "${output_file}"
		fi
        fi

done < "${data_file}"

printf "October births saved to %s\n" "${output_file}"

printf "\nNumber of October births:\n\n"

# tail -n for number of lines +2 means starting from the second line 
# (2 would be the first 2 lines only; -2 would be the last 2 lines only)
# then word count -l lines to get the number of lines i.e. people
tail -n +2 "${output_file}" | wc -l

# add a blank line for output appearance
echo

#pint the headers
head -n 1 "${output_file}"
#print the rest, sorted by column 2 (country) then 1 (name)
tail -n +2 "${output_file}" | sort -t $'\t' -k2,2 -k1,1

echo



