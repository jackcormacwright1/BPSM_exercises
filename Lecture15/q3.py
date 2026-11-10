#!/usr/bin/env python3
# Exercise 3

################################################################################

#Write a Python function that will take a DNA sequence along with an optional threshold 
#and return True or False to indicate whether the DNA sequence contains 
#a high proportion of undetermined bases (i.e not A, T, G or C).

#Write some assertions to test whether the function works.

################################################################################


def has_high_undetermined_bases(dna, threshold=10):
    dna = dna.upper()
 
    if len(dna) == 0:
        raise ValueError("The DNA sequence is empty!!!!!!!!")
 
    if threshold < 0 or threshold > 100:
        raise ValueError("The threshold is a percentage so must be between 0 and 100!!!!!!!!!!")

    undetermined = 0
    for base in dna:
        if base not in "ATGC":
            undetermined = undetermined + 1

    percentage = undetermined / len(dna) * 100
    return percentage > threshold






if __name__ == "__main__":
    assert has_high_undetermined_bases("ATGC") is False         
    assert has_high_undetermined_bases("ATGN") is True          
    assert has_high_undetermined_bases("ATGN", 25) is False     
    assert has_high_undetermined_bases("ATGN", 20) is True      
    assert has_high_undetermined_bases("atgc") is False
    assert has_high_undetermined_bases("ATGR", 20) is True
    assert has_high_undetermined_bases("NNNN", 100) is False

    print("Tests completed")
    print("Does ATGN exceed 10% undetermined bases?", has_high_undetermined_bases("ATGN"))











