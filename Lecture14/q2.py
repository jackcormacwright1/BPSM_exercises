#!/bin/python3

#########################################################################

#exercise 2

# Write a programme/script that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) 
# that occur more than some number of times n (you chose what the number n is!).

########################################################################

import os

os.chdir("/localdisk/home/s1306053/BPSM/exercises/Lecture14")

dna = "ATGCCGCACCGCCATTTTTTTGCCGATATTATGCATTATGGCCCGTCATCCGGATG"
k = 3   # k-mer size
n = 2   # report kmers occurring more than n times
o = 1   # offset

#check the input values are ok
if k <= 0:
    raise ValueError("The k-mer size must be greater than zero.")
if o <= 0:
    raise ValueError("The offset must be greater than zero.")
if n < 0:
    raise ValueError("The occurrence threshold cannot be negative.")

kmers = []
#generate kmers counting from the start up to the final start position (length of sequence minus 1 kmer length)
for start in range(0, len(dna) - k + 1, o):
    kmer = dna[start:start + k]
    kmers.append(kmer)

#build a list of the unique kmers so it remains ordered
unique_kmers = []
for kmer in kmers:
    if kmer not in unique_kmers:
        unique_kmers.append(kmer)

kmer_counts = []
#count occurrences into a list and print out the counts
#the lists are ordered so the index of the unique kmers can
#be used to look up the counts later without a dictionary
for kmer in unique_kmers:
    count = kmers.count(kmer)
    kmer_counts.append(count)
    if count > n:
        print(f"{kmer} occurs {count} times")






