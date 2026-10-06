#!/bin/bash

#Work out how many people were born in October, and where are they from, output as multiple lists

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"
output_dir="./q5_october_births_grouped"

mkdir -p  "${output_dir}"

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
                        decade=$((year / 10 * 10))
			output_file="${output_dir}/${decade}s_births.txt"
			if [[ ! -s "${output_file}" ]]
			then
				printf 'Name\tCountry\tBirth_year\tDecade\n' > "${output_file}"
			fi
			printf '%s\t%s\t%s\t%s\n' "${name}" "${country}" "${year}" "${decade}" >> "${output_file}"
                fi
        fi

done < "${data_file}"

printf "October births split by birth decade and saved to %s\n" "${output_dir}"

echo





