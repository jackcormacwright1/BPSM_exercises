

######################################################################################################

#1. how many fungal species have genomes bigger than 100Mb? What are their names?

######################################################################################################

import pandas as pd

file_path = 'eukaryotes.txt'

# load in the tsv by specifying separated by tab
# the table uses - for blanks so define this as the na_values
df = pd.read_csv(file_path, sep="\t", na_values="-")

# add a new column called species which is the first 2 whitespace delimited strings from the organism name column
df["Species"] = df["#Organism/Name"].str.split().str[:2].str.join(" ")

#pull out the big fungi
fungi_over_100Mb = df[(df["Group"] == "Fungi") & (df["Size (Mb)"] > 100)]

#the number of assemblies is the length as one row per assembly
n_assemblies = len(fungi_over_100Mb)
#nunique gives the number of unique organisms and species
n_organisms = fungi_over_100Mb["#Organism/Name"].nunique()
n_species = fungi_over_100Mb["Species"].nunique()

#to get a summary across assemblies per species group by species and
# aggregate on size for number of rows, mean and max
q1 = (fungi_over_100Mb.groupby("Species")
                .agg(assemblies=("#Organism/Name", "size"),
                     avg_size_mb=("Size (Mb)", "mean"),
                     max_size_mb=("Size (Mb)", "max")
                     )
                .sort_index()
      )


# print out the answer
print("*" * 60)
print()
print(f"There are {n_species} species and {n_organisms} organisms of fungi with genomes bigger than 100Mb!!!!") 
print(f"These are recorded across {n_assemblies} assemblies!!!!!")
print()
print("The species with number of assemblies, mean size and max size:")
print()
print(q1.to_string())
print()
print("*" * 60)






