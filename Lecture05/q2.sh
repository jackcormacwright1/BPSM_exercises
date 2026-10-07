#!/bin/bash

#Go through the file showing an index counter, name, city and the country, but without the header and blanks lines this time

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"

counter=0

while IFS=$'\t' read -r name email city day month year country
do
	#double square brackets indicate a logical test condition (needs the spaces after the bracket)
	#skip if the first column is called name (i.e. headers) or is blank
	if [[ ${name} != "name" && ${name} != "" ]]
	then
        	counter=$((counter + 1))
        	echo -e "${counter}\tNAME-${name}\tCITY-${city}\tCOUNTRY-${country}"
	fi

#output the result in columns based on tab separated
done < "${data_file}" | column -t -s $'\t'







