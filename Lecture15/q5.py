#!/usr/bin/env python3
# Exercise 5: K-mer counting (again!)

#############################################################################################

#K-mers are short DNA subsequences with length "k" bases, and are usually generated 
#using the sliding window method we used in previous lecture exercises.

#Write a Python function that, given any DNA sequence, 
#will print all the k-mers (e.g. 4-mers) that occur more than n times.

#E.g. with dna="ATGCATCATG", kmersize=2 and minfrequency=2 will output
#AT

#because the kmers (kmersize) are 2 bases long, and there are three (minfrequency was 2) instances of "AT"

############################################################################################


def print_frequent_kmers(dna, kmersize, minfrequency):
    if kmersize < 1:
        raise ValueError("The k-mer length must be at least 1.")
    if minfrequency < 0:
        raise ValueError("The frequency threshold must not be negative.")

    dna = dna.upper()
    kmers = []
    
    for start in range(len(dna) - kmersize + 1):
        kmer = dna[start:start + kmersize]
        kmers.append(kmer)

    # store the printed kmers so if it is already printed we dont print the count again
    # could also loop the unique list instead?
    printed = []
    for kmer in kmers:
        if kmers.count(kmer) > minfrequency and kmer not in printed:
            print(kmer)
            printed.append(kmer)





if __name__ == "__main__":
    print_frequent_kmers("ATGCATCATG", 2, 2)  # Expected output: AT






