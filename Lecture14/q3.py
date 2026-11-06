#!/bin/python3

################################################################

# exercise 3

#Here is a list of DNA sequences that are all equal in length, 
#with varying degrees of similarity to each other:
#['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']
#Write a programme/script that calculates and prints, for each pair of sequences, 
#the percentage of identical positions 

################################################################

sequences = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']
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
        
        #work out the % identical of the longer sequence
        max_len = max(len(seq1), len(seq2))
        percentage = (identical / max_len) * 100
        print(f"Pair ({i+1}, {j+1}): {percentage:.1f}% identical (% of the longer sequence - s1={len(seq1)}, s2={len(seq2)})")









