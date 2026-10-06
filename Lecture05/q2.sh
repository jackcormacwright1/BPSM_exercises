#!/bin/bash

#Go through the file showing an index counter, name, city and the country, but without the header and blanks lines this time

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"

counter=0

while IFS=$'\t' read -r name email city day month year country
do
	if [[ ${name} != "name" && ${name} != "" ]]
	then
        	counter=$((counter + 1))
        	echo -e "${counter}\tNAME-${name}\tCITY-${city}\tCOUNTRY-${country}"
	fi

done < "${data_file}" | column -t -s $'\t'







