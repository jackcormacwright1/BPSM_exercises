#!/bin/bash

#Work out how many people were born in October, and where are they from, output as multiple lists

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"
output_dir="./q5_october_births_grouped"

mkdir -p  "${output_dir}"

# clear out the files if they were already created
for file in "${output_dir}"/*s_births.txt
do
    if [[ -f "${file}" ]]
    then
        > "${file}"
    fi
done

while IFS=$'\t' read -r name email city day month year country
do
        if [[ ${name} != "name" && ${name} != "" ]]
        then
                if [[ ${month} = 10 ]]
                then
			# if they are born in october then
			# i have decided to split by decade as most country files would only have one person
			# double brackets for arithmetic and $ to assign variable
			# convert the year to a decade
                        decade=$((year / 10 * 10))
			output_file="${output_dir}/${decade}s_births.txt"
			if [[ ! -s "${output_file}" ]]
			then
				printf 'Name\tCountry\tBirth_year\tDecade\n' > "${output_file}"
			fi
			# add decade in as the new column from the created variable
			printf '%s\t%s\t%s\t%s\n' "${name}" "${country}" "${year}" "${decade}" >> "${output_file}"
                fi
        fi

done < "${data_file}"

printf "October births split by birth decade and saved to %s\n" "${output_dir}"

echo





