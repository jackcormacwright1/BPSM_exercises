#!/bin/bash

#show the HSPs with more than 20 mismatches

data_file="/localdisk/home/s1306053/BPSM/exercises/Lecture06/blastoutput2.out"

counter=0

#file headers:
#query acc.ver, subject acc.ver, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score

printf "Query_Accession_Number\tSubject_Accession_Number\tMismatches\n"

while IFS=$'\t' read -r query_accession subject_accession identity_percent alignment_length mismatches gap_opens q_start q_end s_start s_end evalue bit_score
do
    if [[ -n "$subject_accession" && "$mismatches" -gt 20 ]]; then
        IFS='|' read -ra subject <<< "$subject_accession"

        printf '%s\t%-30s\t%-s\n' \
            "$query_accession" "${subject[3]}" "$mismatches"

        counter=$((counter + 1))
    fi
done < "$data_file"

printf 'Total HSPs with more than 20 mismatches: %s\n' "$counter"


