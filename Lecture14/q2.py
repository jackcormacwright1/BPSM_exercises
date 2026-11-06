#!/bin/python3

#########################################################################

#exercise 2

# Write a programme/script that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) 
# that occur more than some number of times n (you chose what the number n is!).

########################################################################

dna = "ATGCCGCACCGCCATTTTTTTGCCGATATTATGCATTATGGCCCGTCATCCGGATG"
k = 3   # k-mer size
n = 2   # report kmers occurring more than n times
o = 1   # offset

kmers = []

# Generate kmers
for start in range(0, len(dna) - k + 1, o):
    kmer = dna[start:start + k]
    kmers.append(kmer)

# Unique kmers
kmer_set = set(kmers)
kmer_counts = []

# Count occurrences
for kmer in kmer_set:
    count = kmers.count(kmer)
    kmer_counts.append(count)
    if count > n:
        print(f"{kmer} occurs {count} times")






