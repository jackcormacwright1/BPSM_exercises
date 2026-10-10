#!/bin/bash

# list the start positions of all matches where the HSP Subject accession includes the letters string "AEI"

source sourcefile

counter=0

#file headers:
#query acc.ver, subject acc.ver, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score

printf "Index\tSubject_Accession\tQuery_Start\tSubject_Start\n"

while IFS=$'\t' read -r query_accession subject_accession identity_percent alignment_length mismatches gap_opens q_start q_end s_start s_end evalue bit_score
do
	if [[ "${subject_accession}" != "" ]]; then
		IFS=$'|' read -ra subject <<< "${subject_accession}"
		if [[ "${subject[3]}" == *"AEI"* ]]; then
			counter=$((counter + 1))
			printf "%s\t%s\t%s\t%s\n" ${counter} ${subject[3]} ${q_start} ${s_start}
		fi
	fi
done < "${data_file}"



















