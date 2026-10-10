#!/bin/bash
source sourcefile

# Show HSPs shorter than 100 amino acids with more than 20 mismatches
counter=0

printf 'Query_Accession_Number\tSubject_Accession_Number\tMismatches\tAlignment_Length\n'

while IFS=$'\t' read -r query_accession subject_accession identity_percent alignment_length mismatches gap_opens q_start q_end s_start s_end evalue bit_score
do
    if [[ -n "$subject_accession" && "$mismatches" -gt 20 && "$alignment_length" -lt 100 ]]; then
        IFS='|' read -ra subject <<< "$subject_accession"

        printf '%s\t%-30s\t%-15s\t%s\n' \
            "$query_accession" "${subject[3]}" "$mismatches" "$alignment_length"

        counter=$((counter + 1))
    fi
done < "$data_file"

printf 'Total HSPs with more than 20 mismatches and length under 100: %s\n' "$counter"










