#!/bin/python3

sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

motif = "GAATTC"
motif_length = len(motif)

#python starts at 0 so count the positions from 1 by adding 1 to all the indexes
motif_start = sequence.find(motif) + 1

print("Position numbers in these answers start at 1")

print(f"The motif begins at position {motif_start} and finishes at position {motif_start + motif_length - 1}")

#the cut is after the first nucleotide so the cut is start position plus 1
print(f"The cut will be between postion {motif_start} and {motif_start + 1}")

#the second fragment is the total length minus the locus of the last nucleotide in the first fragment (the first character of the motif)
print(f"The length of the first fragment will be {motif_start}")
print(f"The length of the second fragment will be {len(sequence) - motif_start}")


