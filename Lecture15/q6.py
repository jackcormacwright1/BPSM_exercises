#!/usr/bin/env python3
# Exercise 6

#############################################################################

#Write a Python script/programme that, given any DNA sequence, will print 
#a list of k-mers that occur more than some number of times.

#The user should be asked to supply, on the command line, the following:
# 1. the sequence of interest
# 2. the kmer length for analysis
# 3. the threshold frequency of kmers found (i.e. the "more than this number" value)

############################################################################



def print_frequent_kmers(dna, kmersize, minfrequency):
    dna = dna.upper()
    kmers = []
    for start in range(len(dna) - kmersize + 1):
        kmers.append(dna[start:start + kmersize])

    printed = []
    for kmer in kmers:
        if kmers.count(kmer) > minfrequency and kmer not in printed:
            print(kmer)
            printed.append(kmer)

    if len(printed) == 0:
        print("No k-mers occur more than the threshold.")




if __name__ == "__main__":
    
    #input will allow the user to input from the command line
    dna = input("Enter the DNA sequence: ").strip()
    
    try:
        kmersize = int(input("Enter the k-mer length: "))
        minfrequency = int(input("Enter the frequency threshold: "))
    except ValueError:
        print("Whole numbers are needed for the length and threshold!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        if len(dna) == 0:
            print("You have entered a non-empty DNA sequence!!!!!!!!!!!!!!!!!!!!!!!!")
        elif kmersize < 1:
            print("The k-mer length has to be at least 1!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("K-mers occurring more than", minfrequency, "times:")
            print_frequent_kmers(dna, kmersize, minfrequency)

