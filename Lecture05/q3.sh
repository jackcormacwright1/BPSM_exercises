#!/bin/bash

#Put people into separate files: a different file for each country

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"

#where we want the separate files to end up
output_dir="./q3_country_files"

# use -p to create if it doesnt already exist
mkdir -p "${output_dir}"

#loop the .txt files already in the output directory
for file in "${output_dir}"/*.txt
do
    #if the file exists overwrite it as a new empty file 
    #this is so it will not duplicate if the code runs more than once
    #-f checks the file exists
    if [[ -f "${file}" ]]
    then
        > "${file}"
    fi
done

while IFS=$'\t' read -r name email city day month year country
do
        if [[ ${name} != "name" && ${name} != "" ]]
        then
		#build the output file name from the output directory and the country name
		output_file="${output_dir}/${country}.txt"
		#-s is true if the file is not empty so ! -s checks that the file is empty
		#this is so we can output the headers row only as the first row
		if [[ ! -s "${output_file}" ]]
		then
			printf 'Name\tEmail\tCity\tBirth_day\tBirth_month\tBirth_year\tCountry\n' > "${output_file}"
                fi
		#printf is print formatted so will substitute %s for variables called after the string
                printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "${name}" "${email}" "${city}" "${day}" "${month}" "${year}" "${country}" >> "${output_file}"
        fi

done < "${data_file}"

#count the number of files in the output directory for the number of countries
#single brackets mean a command substitution vs double brackets for arithmetic
#dollar sign needed to assign the output of the brackets to the variable
#ls lists the file names one per line
#-l on the word count counts lines
country_count=$(ls -1 "${output_dir}" | wc -l)
printf "%s country files saved to %s" "${country_count}" "${output_dir}"






