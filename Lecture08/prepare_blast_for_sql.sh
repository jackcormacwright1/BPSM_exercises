#!/bin/bash

awk -F'\t' '
BEGIN {OFS=","} 
$1 !~ /^#/
{print $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12}
' "/localdisk/home/s1306053/BPSM/exercises/Lecture08/blastoutput2.out" > blast_output.csv




