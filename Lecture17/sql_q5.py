
######################################################################################################

#5. add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes?
# sql version

######################################################################################################

import os

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

#set up the connection variables to the database
MYSQL_USER = "s1306053"
MYSQL_DB = "s1306053_PandaPlay"
MYSQL_HOST = "129.215.237.85"
TABLE = "eukaryotes"

#get the password that was stored by the orchestrator
password = os.environ.get("MySQL_password")

#build the connection string
url = URL.create(
                "mysql+mysqldb", #driver 
                username=MYSQL_USER, 
                password=password,
                host=MYSQL_HOST, 
                database=MYSQL_DB
                )

engine = create_engine(url)


def query(sql, printout=True, **params):
    '''
    Run a SELECT and return the resulting dataframe
    there is an optional print argument which is defaulted to on
    the function takes the sql string, the optional print argument and additional parameters used in q4
    '''
    #establish the connection
    with engine.connect() as conn:
        #store the result - params is used to dynamically replace tags in the sql script with the passed parameter
        #takes the tag and replacement string as key value pairs
        result = pd.read_sql(text(sql), conn, params=params)
    if printout:
        print(result.to_string(index=False))
    return(result)


# SUBSTRING_INDEX(string, delimiter, n) returns everything before the n-th delimiter
# this can be substituted into the sql queries whenever species is needed
# alternatively could ALTER TABLE and add a column to store it permanently
SPECIES = "SUBSTRING_INDEX(organism, ' ', 2)"



with engine.begin() as conn:
    #add the column with the data type double because we are dividing so it cannot be int
    conn.execute(text(f"ALTER TABLE {TABLE} ADD COLUMN proteins_per_gene DOUBLE"))
    #update the column with the calculation
    conn.execute(text(f"UPDATE {TABLE} SET proteins_per_gene = proteins / genes"))

# print out the answer                                                                            
print("*" * 60)                                                                                   
print()

#the number of assemblies and species
q5 = query(f"""
    SELECT COUNT(*)                  AS assemblies,
           COUNT(DISTINCT {SPECIES}) AS species
    FROM {TABLE}
    WHERE proteins_per_gene >= 1.1
""")

print()

#the assemblies for each group
query(f"""
    SELECT group_name, COUNT(*) AS assemblies
    FROM {TABLE}
    WHERE proteins_per_gene >= 1.1
    GROUP BY group_name
    ORDER BY assemblies DESC
""")

print()

#the top 15 rows ordered with the highest first
print("Top 15 by proteins per gene:")
query(f"""
    SELECT organism, group_name, assembly_accession,
           CAST(genes AS UNSIGNED)     AS genes,
           CAST(proteins AS UNSIGNED)  AS proteins,
           ROUND(proteins_per_gene, 3) AS ratio
    FROM {TABLE}
    WHERE proteins_per_gene >= 1.1
    ORDER BY proteins_per_gene DESC
    LIMIT 15
""")

print()
#iloc[0] gives the first value i.e. the total number of assemblies and total number of species from the grouped count
print(f"{q5["assemblies"].iloc[0]} assemblies have >= 10% more proteins than genes ({q5["species"].iloc[0]} species)\n")
print()
print("*" * 60)






