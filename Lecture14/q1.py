#!/bin/python3

###################################################################

# 1 - Print out the gene names for all genes from the species 
#       Drosophila melanogaster or Drosophila simulans.
# 2 - Print out the gene names for all genes that are 
#       between 90 and 110 bases long.
# 3 - Print out the gene names for all genes whose AT content is 
#       less than 0.5 and whose expression level is greater than 200.
# 4 - Print out the gene names for all genes whose name begins 
#       with "k" or "h" except those belonging to Drosophila melanogaster.
# 5 - For each gene, print out a message giving the gene name and 
#       saying whether its AT content is high (greater than 0.65), 
#       low (less than 0.45) or medium (between 0.45 and 0.65).

##################################################################

import os

os.chdir("/localdisk/home/s1306053/BPSM/exercises/Lecture14")

data_path = "data.csv"

target_species = ['Drosophila melanogaster', 'Drosophila simulans']

melanogaster_genes = []
simulans_genes = []
genes_ninety_to_oneten_length = []
low_at_high_exp = []
start_kh_not_melanogaster = []
at_categories = []

with open(data_path, "r") as file:
    # read each line of the dna file
    for line in file:
        # get the columns into different values
        species_name, sequence, gene_name, expression_level = line.split(",")

        # store part 1 answers
        if species_name == target_species[0]:
            melanogaster_genes.append(gene_name)
        elif species_name == target_species[1]:
            simulans_genes.append(gene_name)

        # store part 2 answers
        if 90 <= len(sequence) <= 110:
            genes_ninety_to_oneten_length.append(gene_name)

        # store part 3 answers
        #calculate AT content
        at_content = (
                sequence.upper().count("A") + sequence.upper().count("T")
                ) / len(sequence)
        if int(expression_level) > 200 and at_content < 0.5:
            low_at_high_exp.append(gene_name)

        # store part 4 answers
        if (
                species_name != 'Drosophila melanogaster' 
                and gene_name.lower().startswith(("k","h"))
        ):
            start_kh_not_melanogaster.append(gene_name)

        # store part 5 answers
        if at_content > 0.65:
            at_category = "Greater than 0.65"
        elif at_content >= 0.45:
            at_category = "Between 0.45 and 0.65"
        else:
            at_category = "Less than 0.45"

        at_categories.append(f"{gene_name}: AT content is {at_category} ({100*at_content:.3f}%)") 

    print("=" * 30)
    print("\nPart 1 Answer\n")

    if len(melanogaster_genes) > 0:
        print(f"There are {len(melanogaster_genes)} melanogaster genes:\n{"\n".join(melanogaster_genes)}\n")
    else:
        print("No melanogaster genes found\n")

    if len(simulans_genes) > 0:
        print(f"There are {len(simulans_genes)} simulans genes:\n{"\n".join(simulans_genes)}\n")
    else:
        print("No simulans genes found\n")

    print("=" * 30)
    print("\nPart 2 Answer\n")

    if len(genes_ninety_to_oneten_length) > 0:
        print(f"There are {len(genes_ninety_to_oneten_length)} genes with length between 90 and 110:\n{"\n".join(genes_ninety_to_oneten_length)}\n")
    else:
        print("No genes found with length between 90 and 110\n")

    print("=" * 30)
    print("\nPart 3 Answer\n")

    if len(low_at_high_exp) > 0:
        print(f"There are {len(low_at_high_exp)} genes with AT content less than 0.5 and expression level greater than 200:\n{"\n".join(low_at_high_exp)}\n")
    else:
        print("No genes found with AT content less than 0.5 and expression level greater than 200\n")

    print("=" * 30)
    print("\nPart 4 Answer\n")

    if len(start_kh_not_melanogaster) > 0:
        print(f"There are {len(start_kh_not_melanogaster)} genes not melanogaster and starting with k or h:\n{"\n".join(start_kh_not_melanogaster)}\n")
    else:
        print("No genes found starting with k or h and not melanogaster\n")

    print("=" * 30)
    print("\nPart 5 Answer\n")

    if len(at_categories) > 0:
        print(f"There are {len(at_categories)} genes :\n{"\n".join(at_categories)}\n")
    else:
        print("No genes found\n")



