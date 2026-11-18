
######################################################################################################

#5. add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes?

######################################################################################################

import pandas as pd

file_path = 'eukaryotes.txt'

# load in the tsv by specifying separated by tab
# the table uses - for blanks so define this as the na_values
df = pd.read_csv(file_path, sep="\t", na_values="-")

# add a new column called species which is the first 2 whitespace delimited strings from the organism name column
df["Species"] = df["#Organism/Name"].str.split().str[:2].str.join(" ")


df["Proteins per gene"] = df["Proteins"] / df["Genes"]
more_proteins = (df[df["Proteins per gene"] >= 1.1].sort_values("Proteins per gene", ascending=False))

cols = ["#Organism/Name", "Group", "Assembly Accession", "Genes", "Proteins", "Proteins per gene"]
q5 = more_proteins[cols].astype({"Genes": int, "Proteins": int}).round({"Proteins per gene": 3})


# print out the answer
print("*" * 60)
print()
print(f"{len(more_proteins):,} assemblies have >= 10% more proteins than genes ({more_proteins['Species'].nunique()} species)\n")
print()
print(more_proteins["Group"].value_counts().to_string())
print()
print("The top 15 assemblies by ratio of proteins to genes:")
print(q5.head(15).to_string(index=False))
print()
print("*" * 60)






