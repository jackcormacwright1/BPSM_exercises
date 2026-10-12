#!/bin/bash

source sourcefile

#list the subject accession for all HSPs

counter=0

#file headers:
#query acc.ver, subject acc.ver, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score

while IFS=$'\t' read -r query_accession subject_accession identity_percent alignment_length mismatches gap_opens q_start q_end s_start s_end evalue bit_score
do
        #column 2 is not blank so exclude blanks and comment lines - the headers are a comment line so no need to exclude
	if [[ "${subject_accession}" != "" ]] then

		#the subject accession has an old ID part and a new ID part in the third pipe delimited section so just take the new ID and return to the screen
		IFS=$'|' read -ra subject <<< "${subject_accession}"
		echo "${subject[3]}"
	fi
done < "${data_file}"



















