#!/bin/bash

#Go through the file showing an index counter and the country

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"

counter=0

while IFS=$'\t' read -r name email city day month year country
do
	counter=$((counter = counter + 1))
	echo "${counter}: ${country}"
done < "${data_file}"



















