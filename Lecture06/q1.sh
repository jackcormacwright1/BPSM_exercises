#!/bin/bash

data_file="/localdisk/home/s1306053/BPSM/exercises/Lecture06/blastoutput2.out"

counter=0

#file headers:
#query acc.ver, subject acc.ver, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score

while IFS=$'\t' read -r query_accession subject_accession identity_percent alignment_length mismatches gap_opens q_start q_end s_start s_end evalue bit_score
do
	if [[ "${subject_accession}" != "" ]] then
		IFS=$'|' read -ra subject
		echo "${subject[3]}" <<< "${subject_accession}"
	fi
done < "${data_file}"



















