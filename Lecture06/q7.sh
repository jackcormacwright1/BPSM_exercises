#!/bin/bash
source sourcefile

# list the top ten highest (best) HSPs.

counter=0

# set the significance value to compare against - this is the cuttoff for significance
significance_value="1e-5"

# save a sorted version of the file - t for the field terminator, n for numeric and r for reversed
sort -t $'\t' -k12,12nr "$data_file" > sorted_hsps.tsv

printf 'Index\tQuery\tSubject\tIdentity_%%\tAlignment_Length\tE-value\tBit_Score\tSignificant\n'

while IFS=$'\t' read -r query_accession subject_accession identity_percent alignment_length mismatches gap_opens q_start q_end s_start s_end evalue bit_score
do
    # exclude comment rows - #* is a hash followed by anything and the \ makes it literal
    [[ "${query_accession}" == \#* ]] && continue
    # -z tests whether a string is empty so skip empty rows
    [[ -z "${subject_accession}" ]] && continue

    IFS='|' read -ra subject <<< "${subject_accession}"

    # to start with assume it is not significant
    significant="no"

    # get which is smaller - the significance value or the row's evalue
    # get the significance value and evalue on 2 lines
    # sort them with -g for scientific notation
    # then choose the value from the first row, i.e. the smaller of the two
    smallest=$(printf '%s\n' "${significance_value}" "${evalue}" | sort -g | head -n 1)

    if [[ "$smallest" != "1e-5" ]]; then
        significant="yes"
    fi

    counter=$((counter + 1))

    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
        "$counter" "$query_accession" "${subject[3]}" "$identity_percent" "$alignment_length" \
        "$evalue" "$bit_score" "$significant"

    if [[ "$counter" -eq 10 ]]; then
        break
    fi
done < sorted_hsps.tsv
