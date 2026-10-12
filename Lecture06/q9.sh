#!/bin/bash
source sourcefile

# how many subject sequences have more than one HSP?

#declare an array for the counts per ID
declare -A counts

while IFS=$'\t' read -r query_accession subject_accession identity_percent alignment_length mismatches gap_opens q_start q_end s_start s_end evalue bit_score
do
    # if it is a comment line (hash followed by something) then skip to next loop item
    [[ "$query_accession" == \#* ]] && continue
    # if it is blank (-z is true for blanks) then skip to next loop item
    [[ -z "$subject_accession" ]] && continue

    IFS='|' read -ra subject <<< "$subject_accession"
    accession="${subject[3]}"

    # increment the array value for the subject accession ID tag
    counts["$accession"]=$(( ${counts["$accession"]} + 1 ))

done < "$data_file"

printf 'Subject_Accession\tHSP_Count\n'

#variable to count how many ended up in the array
multiple=0

# @ for all the elements of the array and ! to loop the keys instead of values
for accession in "${!counts[@]}"
do
    if [[ "${counts[$accession]}" -gt 1 ]]; then
        printf '%s\t%s\n' "$accession" "${counts[$accession]}"
        multiple=$((multiple + 1))
    fi
done

printf 'Subjects with multiple HSPs: %s\n' "$multiple"
