#!/bin/bash
source sourcefile

# allocate HSPs into a small number of different groups based on their scores (you choose which scores)

# score categories came from https://blast.ncbi.nlm.nih.gov/doc/blast-quick-start-guide/results_grapicsummary.html

output_dir="q11_output"
mkdir -p "$output_dir"

# Empty the files so rerunning the script doesn't duplicate results
for group in very_weak weak moderate strong very_strong
do
    > "$output_dir/$group.tsv"
done

declare -A counts

while IFS= read -r line
do
    [[ "$line" == \#* ]] && continue
    [[ -z "$line" ]] && continue

    IFS=$'\t' read -r query_accession subject_accession identity_percent alignment_length mismatches gap_opens q_start q_end s_start s_end evalue bit_score <<< "$line"

    [[ -z "$subject_accession" ]] && continue

    score_integer="${bit_score%.*}"

    if [[ "$score_integer" -lt 40 ]]; then
        group="very_weak"
    elif [[ "$score_integer" -lt 50 ]]; then
        group="weak"
    elif [[ "$score_integer" -lt 80 ]]; then
        group="moderate"
    elif [[ "$score_integer" -lt 200 ]]; then
        group="strong"
    else
        group="very_strong"
    fi

    counts["$group"]=$(( ${counts["$group"]} + 1 ))
    printf '%s\n' "$line" >> "$output_dir/$group.tsv"
done < "$data_file"

{
    printf 'Group\tBit_Score_Range\tHSP_Count\n'
    printf 'Very weak\t<40\t%s\n' "${counts[very_weak]:-0}"
    printf 'Weak\t40–<50\t%s\n' "${counts[weak]:-0}"
    printf 'Moderate\t50–<80\t%s\n' "${counts[moderate]:-0}"
    printf 'Strong\t80–<200\t%s\n' "${counts[strong]:-0}"
    printf 'Very strong\t>=200\t%s\n' "${counts[very_strong]:-0}"
} | column -t -s $'\t'





