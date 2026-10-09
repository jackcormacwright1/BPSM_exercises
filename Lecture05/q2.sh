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
        	# %-6s means substitute padded with 6 spaces"
        	# - means left-aligned
        	printf '%-6s%-40s%-35s%s\n' "${counter}" "NAME-${name}" "CITY-${city}" "COUNTRY-${country}"
	fi

done < "${data_file}"



