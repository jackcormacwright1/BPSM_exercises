#!/bin/python3

######################################################################################################

#4. which sequencing centre has sequenced the most plant genomes? the most insect genomes?

######################################################################################################

import pandas as pd

file_path = 'eukaryotes.txt'

# load in the tsv by specifying separated by tab
# the table uses - for blanks so define this as the na_values
df = pd.read_csv(file_path, sep="\t", na_values="-")

# add a new column called species which is the first 2 whitespace delimited strings from the organism name column
df["Species"] = df["#Organism/Name"].str.split().str[:2].str.join(" ")


def get_top_sequencers(df, category, level, top_n=1):
    dataset = df
    group_dataset = dataset[dataset[level] == category]
    top_dataset = group_dataset["Center"].str.upper().str.strip().value_counts().head(top_n)
    
    #print outputs
    print(f"Most {category.lower()}: {top_dataset.index[0]} ({top_dataset.iloc[0]})")
    return(top_dataset)


targets = {
            "Plants": "Group",
            "Insects": "SubGroup"
            }

# print out the answer
print("*" * 60)
print()
for category in targets:
    print(f"The sequencing centre that has sequenced the most {category.lower()}:")
    get_top_sequencers(df, category=category, level=targets.get(category))
    print()
print("*" * 60)






