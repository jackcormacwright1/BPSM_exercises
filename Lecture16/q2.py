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

# input - codon usage table
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



#translate the sequence into proteins
def translate(sequence, frame, genetic_code):
    '''
    this function translates a DNA sequence into a protein amino acid residue string

    it takes as argumemts:
        sequence = the dna sequence (string)
        frame = the number start position of the frame (int)
        genetic_code = the translation dictionary between DNA codons and amino acid residue codes (dictionary)

    steps:
        1. initialise an empty string to store the protein sequence
        2. loop the sequence start positions based on the frame up to the last complete codon
        3. slice the codon out of the sequence
        4. use .get to look up the amino acid value using the codon as the key
            and replace with X if not found
        5. append the amino acid to the protein string
        6. return the protein string

    '''
    protein = ""

    #move three bases at a time stopping before an incomplete codon
    for position in range(frame, len(sequence) - 3 + 1, 3):
        codon = sequence[position:position + 3]
        amino_acid = genetic_code.get(codon, "X")
        protein += amino_acid

    return protein


def reverse_complement(sequence):
    '''
    this function converts a DNA sequence to its complement

    it takes as arguments:
        sequence = the dna sequence (string)

    steps:
        1. initialise a dictionary mapping nucleotide codes to their complement codes
        2. initialise a string to store the reversed DNA string (complement)
        3. loop the whole sequence stepping from the end backwards one character at a time
        4. use .get to look up the complementary base from the dictionary
        5. append to the reverse strand string
        6. return the reverse strand string

    '''
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


# get a user input dna sequence and quality control to remove spaces and convert all to upper case
dna = input("Enter a DNA sequence: ")
dna = "".join(dna.split()).upper()

# get the reverse complementary string of the input sequence
reverse_dna = reverse_complement(dna)

print("\nForward frames")
# loop the 3 frames and translate to protein + print
for frame in range(3):
    protein = translate(dna, frame, gencode)
    print(f"+{frame + 1}: {protein}")

# loop the 3 frames on the reversed dna and translate + print
print("\nReverse frames")
for frame in range(3):
    protein = translate(reverse_dna, frame, gencode)
    print(f"-{frame + 1}: {protein}")









