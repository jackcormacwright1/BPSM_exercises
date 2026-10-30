#!/bin/python3

line1 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCT"
line2 = "ACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCT"
line3 = "ATCATCGATCGATATCGATGCATCGACTACTAT"

sequence = line1 + line2 + line3

#the first exon is up to 63. this would be up to 62 as it starts counting at 0 but the upper slice position is not included so back to 63
exon1 = sequence[:63]
#the second exon starts at the 91st character so take from 90 on as counting starts from 0
exon2 = sequence[90:]

coding_sequence = exon1 + exon2
print(f"The coding sequence is: {coding_sequence}")

coding_length = len(coding_sequence)
print(f"The length of the coding sequence is: {coding_length}")

coding_percentage = coding_length / len(sequence)
print(f"The percentage of the sequence that is coding is: {coding_percentage:.2%}")

intron = sequence[63:90]

case_sequence = exon1 + intron.lower() + exon2

print("The original sequence was:")
print(sequence)
print("The sequence with introns in lower case and exons in upper case is:")
print(case_sequence)


