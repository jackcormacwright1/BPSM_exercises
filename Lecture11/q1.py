#!/bin/python3

sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

a_nucleotides = sequence.count("A")
t_nucleotides = sequence.count("T")

print(f"There are {a_nucleotides} A nucleotides")

print(f"There are {t_nucleotides} T nucleotides")

total_nucleotides = len(sequence)
a_t_nucleotides = a_nucleotides + t_nucleotides
percentage_a_t = a_t_nucleotides / total_nucleotides

print(f"There are {percentage_a_t:.2%} A and T nucleotides")









