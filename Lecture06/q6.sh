#!/bin/bash
source sourcefile

#how many HSPs are shorter than 100 amino acids?
counter=0

while IFS=$'\t' read -r query_accession subject_accession identity_percent alignment_length mismatches gap_opens q_start q_end s_start s_end evalue bit_score
do
    if [[ -n "$subject_accession" && "$alignment_length" -lt 100 ]]; then
        counter=$((counter + 1))
    fi
done < "$data_file"

printf 'Total HSPs with fewer than 100 amino acids: %s\n' "$counter"










