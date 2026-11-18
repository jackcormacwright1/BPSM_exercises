
######################################################################################################

#3. which Heliconius species genomes have been sequenced?

######################################################################################################

import pandas as pd

file_path = 'eukaryotes.txt'

# load in the tsv by specifying separated by tab
# the table uses - for blanks so define this as the na_values
df = pd.read_csv(file_path, sep="\t", na_values="-")

# add a new column called species which is the first 2 whitespace delimited strings from the organism name column
df["Species"] = df["#Organism/Name"].str.split().str[:2].str.join(" ")


helic = df[df["#Organism/Name"].str.startswith("Heliconius ")]

q3 = (helic.groupby("Species")
           .agg(assemblies=("#Organism/Name", "size"),
                subspecies_or_strains=("#Organism/Name", "nunique")
                )
           .sort_values(["assemblies", "subspecies_or_strains"], ascending=False)
      )


# print out the answer
print("*" * 60)
print()
print("The heliconius species genomes that have been sequenced are:")
print()
print(q3.to_string())
print()
print("*" * 60)






