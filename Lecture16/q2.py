#!/bin/python

#####################################################################

#Write a Python programme/script that will take any DNA sequence 
#and translate it into protein using the translation table.

#What happens if the DNA sequence contains undetermined bases (e.g. N)?

#Can you generate a translation in all three "forward" frames 
#(transcription is on the top strand, starting at base 1, 2, and 3)?

#Can you generate a translation in all three "reverse" frames 
#(transcription is on the bottom strand, starting at base end, end-1, and end-2)?

######################################################################


gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}



def translate(sequence, frame, genetic_code):
    protein = ""

    #move three bases at a time stopping before an incomplete codon
    for position in range(frame, len(sequence) - 3 + 1, 3):
        codon = sequence[position:position + 3]
        amino_acid = genetic_code.get(codon, "X")
        protein += amino_acid

    return protein


def reverse_complement(sequence):
    complements = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    reverse_strand = ""

    for base in sequence[::-1]:
        reverse_strand += complements.get(base, "N")

    return reverse_strand


dna = input("Enter a DNA sequence: ")
dna = "".join(dna.split()).upper()

reverse_dna = reverse_complement(dna)

print("\nForward frames")
for frame in range(3):
    protein = translate(dna, frame, gencode)
    print(f"+{frame + 1}: {protein}")

print("\nReverse frames")
for frame in range(3):
    protein = translate(reverse_dna, frame, gencode)
    print(f"-{frame + 1}: {protein}")









