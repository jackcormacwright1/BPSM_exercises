#!/bin/bash
source sourcefile

while IFS=$'\t' read -r query_accession subject_accession identity_percent alignment_length mismatches gap_opens q_start q_end s_start s_end evalue bit_score
do
    [[ "${query_accession}" == \#* ]] && continue
    [[ -z "${subject_accession}" ]] && continue

    IFS='|' read -ra subject <<< "${subject_accession}"

    mismatch_percent=$((100 * "${mismatches}" / "${alignment_length}"))

    printf '%s\t%s\t%s\t%s\n' \
        "${subject[3]}" "${mismatches}" "${alignment_length}" "${mismatch_percent}"
done < "${data_file}" |
sort -t $'\t' -k4,4nr |
{
    count=0
    
    printf 'Index\tSubject_Accession\tMismatches\tAlignment_Length\tMismatch_Percent\n'
    
    while IFS=$'\t' read -r accession mismatches alignment_length mismatch_percent
    do
        count=$((count + 1))

        printf '%s\t%s\t%s\t%s\t%s\n' \
            "${count}" "${accession}" "${mismatches}" "${alignment_length}" "${mismatch_percent}"
    done
} | 
column -t -s $'\t'











