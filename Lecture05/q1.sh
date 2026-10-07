#!/bin/bash

#Go through the file showing an index counter and the country

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"

counter=0

#while loop over the countries and store the index in an incrementing counter
#set IFS inside the while loop so it doesnt have to be reset after - only applies inside the loop
#needed before the '\t' to say interpret this as a tab together not separate characters
#read -r for raw to treat backslashes in the data as ordinary characters
while IFS=$'\t' read -r name email city day month year country
do
	#counter increments itself on every new line
	#double brackets indicate arithmetic
	#dollar sign needed to assign the bracket output to the variable
	counter=$((counter + 1))
	echo "${counter}: ${country}"
done < "${data_file}"



















