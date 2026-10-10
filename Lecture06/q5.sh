#!/bin/bash
source sourcefile

# list the first 20 HSPs that have fewer than 20 mismatches
counter=0

printf 'Index\tQuery_Accession_Number\tSubject_Accession_Number\tMismatches\tAlignment_Length\n'

while IFS=$'\t' read -r query_accession subject_accession identity_percent alignment_length mismatches gap_opens q_start q_end s_start s_end evalue bit_score
do
    if [[ -n "$subject_accession" && "$mismatches" -lt 20 ]]; then
        IFS='|' read -ra subject <<< "$subject_accession"

        counter=$((counter + 1))

        printf '%s\t%s\t%-30s\t%-15s\t%s\n' \
            "${counter}" "$query_accession" "${subject[3]}" "$mismatches" "$alignment_length"
    

        if [[ "$counter" -eq 20 ]]; then
            break
        fi   

    fi
done < "$data_file"











