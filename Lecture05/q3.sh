#!/bin/bash

#Put people into separate files: a different file for each country

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"

output_dir="./q3_country_files"

mkdir -p "${output_dir}"

for file in "${output_dir}"/*.txt
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
		output_file="${output_dir}/${country}.txt"
		if [[ ! -s "${output_file}" ]]
		then
			printf 'Name\tEmail\tCity\tBirth_day\tBirth_month\tBirth_year\tCountry\n' > "${output_file}"
                fi
                printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "${name}" "${email}" "${city}" "${day}" "${month}" "${year}" "${country}" >> "${output_file}"
        fi

done < "${data_file}"


country_count=$(ls -1 "${output_dir}" | wc -l)
printf "%s country files saved to %s" "${country_count}" "${output_dir}"






