#!/bin/python3

sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

sequence = sequence.lower()

complement = sequence.replace("a","T")
complement = complement.replace("t","A")
complement = complement.replace("c","G")
complement = complement.replace("g","C")

print(f"The complement of the sequence is {complement}")


