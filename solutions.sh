#!/bin/bash

# Location of the source data
DATA="../../BPSM03/example_people_data.tsv"

echo "Q1: How many people are there?"

awk -F'\t' '
NR > 1 && NF > 0 {
    count++
}
END {
    print count+0
}
' "$DATA"

echo

echo "Q2: How many people are aged around 30 or older?"

awk -F'\t' '
NR > 1 && NF > 0 {
    dob = $6 * 10000 + $5 * 100 + $4

    if (dob <= 19961001) {
        count++
    }
}
END {
    print count+0
}
' "$DATA"

echo

echo "Q3: How many people are called Jan?"

awk -F'\t' '
NR > 1 && $1 == "Jan" {
    count++
}
END {
    print count+0
}
' "$DATA"

echo

echo "Q4: What is the most common country of birth, and how many people from that country are around 50 or older?"

top_country=$(
    awk -F'\t' '
    NR > 1 && NF > 0 {
        count[$7]++

        if (count[$7] > max) {
            max = count[$7]
            top = $7
        }
    }
    END {
        print top
    }
    ' "$DATA"
)

echo "Most common country: $top_country"

awk -F'\t' -v country="$top_country" '
NR > 1 && NF > 0 && $7 == country && $6 <= 1976 {
    count++
}
END {
    print "Around 50 or older:", count+0
}
' "$DATA"

echo

echo "Q5: People with edu email addresses, reverse alphabetical order within country"

mkdir -p results
{
printf "Name\tEmail\tCountry\n"
awk -F'\t' '
BEGIN {
    OFS = "\t"
}
NR > 1 && $2 ~ /edu/ {
    print $1, $2, $7
}
' "$DATA" |
sort -t$'\t' -k3,3 -k1,1r 
} > results/edu_email_addresses_by_country.tsv

echo "$(tail -n +2 results/edu_email_addresses_by_country.tsv | grep -c .) email addresses found"

echo
echo "Q5 results saved at results/edu_email_addresses_by_country.tsv"

echo
echo
