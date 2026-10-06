#!/bin/bash

#Go through the file showing an index counter and the country



counter=0

while IFS='\t' read name email city day month year country
do
	counter=$((counter++))























