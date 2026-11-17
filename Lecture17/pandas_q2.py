#!/bin/python3

######################################################################################################

# 2. how many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?

######################################################################################################

import pandas as pd

file_path = 'eukaryotes.txt'

# load in the tsv by specifying separated by tab
# the table uses - for blanks so define this as the na_values
df = pd.read_csv(file_path, sep="\t", na_values="-")

# add a new column called species which is the first 2 whitespace delimited strings from the organism name column
df["Species"] = df["#Organism/Name"].str.split().str[:2].str.join(" ")

q2 = (df.groupby("Group")
        .agg(assemblies=("#Organism/Name", "size"),
             species=("Species", "nunique")
             )
        .sort_values("assemblies", ascending=False)
      )

# print out the answer
print("*" * 60)
print()
print("The number of each kingdom/group sequenced are:")
print()
print(q2.to_string())
print()
print("*" * 60)






