#!/bin/bash

data_file="/localdisk/home/s1306053/BPSM/exercises/Lecture06/blastoutput2.out"

counter=0

#file headers:
#query acc.ver, subject acc.ver, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score

printf "Query_Accession_Number\tAlignment_Length\tPercent_Identity\n"

while IFS=$'\t' read -r query_accession subject_accession identity_percent alignment_length mismatches gap_opens q_start q_end s_start s_end evalue bit_score
do
        if [[ "${subject_accession}" != "" ]] then
                printf "%s\t%-20s\t%s\n" "${query_accession}" "${alignment_length}" "${identity_percent}"
        fi
done < "${data_file}"


































