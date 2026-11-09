#!/bin/python3

################################################################

# exercise 3

#Here is a list of DNA sequences that are all equal in length, 
#with varying degrees of similarity to each other:
#['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']
#Write a programme/script that calculates and prints, for each pair of sequences, 
#the percentage of identical positions 

################################################################

import os

os.chdir("/localdisk/home/s1306053/BPSM/exercises/Lecture14")

sequences = ['ATTGTACGGGGG', 'AATGAACCGGG', 'AATGAACCC', 'AATGGGAAT']
n = len(sequences)

#loop all pairs of sequences
for i in range(n):
    for j in range(i + 1, n):
        # get each sequence
        seq1 = sequences[i]
        seq2 = sequences[j]
        
        # work out which one is the shortest if they are different lengths
        min_len = min(len(seq1), len(seq2))
        
        #count the identical characters
        identical = 0

        for k in range(min_len):
            if seq1[k] == seq2[k]:
                identical += 1

        if len(seq1) > len(seq2):
            denominator_message = f"length of sequence {i + 1} (the longer sequence)"
        elif len(seq2) > len(seq1):
            denominator_message = f"length of sequence {j + 1} (the longer sequence)"
        else:
            denominator_message = f"length of either sequence (both have equal length)"

        #work out the % identical of the longer sequence
        max_len = max(len(seq1), len(seq2))
        
        #test for a divide by zero error
        try:
            percentage = (identical / max_len) * 100
        except ZeroDivisionError:
            print(f"Pair ({i+1}, {j+1}): both sequences are empty")
        else:
            print(f"Pair ({i+1}, {j+1}): {percentage:.1f}% identical")
            print(f"(denominator = {denominator_message}, {max_len})\n")









