
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

#define a function to get the top sequencing centres for a given column (level) and value (category)
def get_top_sequencers(df, category, level, top_n=1):
    '''
    function takes a dataframe, value such as Plants, level such as Group and top_n int
    the level is the column to look for and the value is the value to look for in that column
    the function prints the output as well as returning the dataframe of the result
    '''
    dataset = df
    #subset the dataframe
    group_dataset = dataset[dataset[level] == category]
    #value counts gives the count per value of the center column - returns ordered highest to lowest
    #head restricts it to the top n passed to the function
    top_dataset = group_dataset["Center"].str.upper().str.strip().value_counts().head(top_n)
    
    #print outputs - index 0 is the name of the top centre and iloc[0] is the first value - i.e. top
    print(f"Most {category.lower()}: {top_dataset.index[0]} ({top_dataset.iloc[0]})")
    return(top_dataset)

#dictionary of pairs to pass to the lookup function
targets = {
            "Plants": "Group",
            "Insects": "SubGroup"
            }

# print out the answer
print("*" * 60)
print()
#loop the targets
for category in targets:
    print(f"The sequencing centre that has sequenced the most {category.lower()}:")
    get_top_sequencers(df, category=category, level=targets.get(category))
    print()
print("*" * 60)






