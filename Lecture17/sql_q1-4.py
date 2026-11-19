################################################################################
#   1. How many fungal species have genomes bigger than 100Mb? What are their names?
#   2. How many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?
#   3. Which Heliconius species genomes have been sequenced?
#   4. Which sequencing centre has sequenced the most plant genomes? The most insect genomes?
################################################################################

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


################################################################################
# Q1. Fungal species with genomes bigger than 100 Mb
################################################################################

print("=" * 80)
print("Q1. Fungal genomes bigger than 100 Mb")
print("=" * 80)

#run the query function - printout defaults to true so it will print the result
query(f'''
    SELECT COUNT(*)                   AS assemblies,
           COUNT(DISTINCT organism)   AS organism_names,
           COUNT(DISTINCT {SPECIES})  AS species
    FROM {TABLE}
    WHERE group_name = 'Fungi' AND size_mb > 100
''')

query(f'''
    SELECT {SPECIES}     AS species,
           COUNT(*)      AS assemblies,
           MAX(size_mb)  AS max_size_mb
    FROM {TABLE}
    WHERE group_name = 'Fungi' AND size_mb > 100
    GROUP BY species
    ORDER BY species
''')


################################################################################
# Q2. Number sequenced per Kingdom/group
################################################################################

print("=" * 80)
print("Q2. Genomes sequenced per group")
print("=" * 80)

query(f'''
    SELECT group_name,
           COUNT(*)                  AS assemblies,
           COUNT(DISTINCT {SPECIES}) AS species
    FROM {TABLE}
    GROUP BY group_name
    ORDER BY assemblies DESC
''')


################################################################################
# Q3. Heliconius genomes
################################################################################

print("=" * 80)
print("Q3. Heliconius species sequenced")
print("=" * 80)

query(f'''
    SELECT COUNT(*)                  AS assemblies,
           COUNT(DISTINCT organism)  AS organism_names,
           COUNT(DISTINCT {SPECIES}) AS species
    FROM {TABLE}
    WHERE organism LIKE 'Heliconius %'
''')

query(f'''
    SELECT {SPECIES}                 AS species,
           COUNT(*)                  AS assemblies,
           COUNT(DISTINCT organism)  AS subspecies_or_strains
    FROM {TABLE}
    WHERE organism LIKE 'Heliconius %'
    GROUP BY species
    ORDER BY assemblies DESC, subspecies_or_strains DESC, species
''')


################################################################################
# Q4. Sequencing centres: most plant genomes, most insect genomes
################################################################################

print("=" * 80)
print("Q4. Top sequencing centres")
print("=" * 80)

#loop a list of tuples containing the column and lookup values and pass the category to params
#from pandas documentation: For parameterized query, using params is recommended over string interpolation.
# the :category tag is replaced by the value passed to params, e.g. Plants
# this is safer because the category is a string which could contain apostrophes, escape characters, SQL injection etc
for level, category in [("group_name", "Plants"), ("subgroup", "Insects")]:
    print(f"The centre with the most genomes where\nlevel = {level}, category = {category}:")
    query(f"""
        SELECT center, COUNT(*) AS assemblies
        FROM {TABLE}
        WHERE {level} = :category AND center IS NOT NULL
        GROUP BY center
        ORDER BY assemblies DESC, center
        LIMIT 1
    """, category=category)







