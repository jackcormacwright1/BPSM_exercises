#!/bin/bash

#Work out how many people were born in October, and where are they from, output as multiple lists

data_file="/home/s1306053/BPSM/BPSM03/example_people_data.tsv"

# single brackets are a command substitution; the dollar assigns the result to a variable

october_births=$(
while IFS=$'\t' read -r name email city day month year country
do
    # skip the header and blank lines
    if [[ ${name} != "name" && ${name} != "" ]]
    then
        if [[ ${month} = 10 ]]
        then
            printf '%s\t%s\n' "${name}" "${country}"
        fi
    fi
done < "${data_file}"
)

# grep -c . counts lines with at least one character (-c to count and . matches any character),
count=$(printf '%s\n' "${october_births}" | grep -c .)

printf 'Number of people born in October: %s\n' "${count}"

# cut -f1 keeps only the first column - f for field and the default is tab delimited
printf '\nNames:\n'
printf '%s\n' "${october_births}" | cut -f1

# sort puts the same countries next to each other so that uniq -c can count them as it only sees the next line
printf '\nCountries:\n'
printf '%s\n' "${october_births}" | cut -f2 | sort | uniq -c

echo
