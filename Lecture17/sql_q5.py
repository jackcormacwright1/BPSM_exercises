
######################################################################################################

#5. add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes?
# sql version

######################################################################################################

import os

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

MYSQL_USER = "s1306053"
MYSQL_DB = "s1306053_PandaPlay"
MYSQL_HOST = "129.215.237.85"
TABLE = "eukaryotes"


password = os.environ.get("MySQL_password")

url = URL.create(
                "mysql+mysqldb", 
                username=MYSQL_USER, 
                password=password,
                host=MYSQL_HOST, 
                database=MYSQL_DB
                )

engine = create_engine(url)


def query(sql, printout=True, **params):
    """Run a SELECT and return the result as a pandas dataframe."""
    with engine.connect() as conn:
        result = pd.read_sql(text(sql), conn, params=params)
    if printout:
        print(result.to_string(index=False))
    return(result)


# SUBSTRING_INDEX(string, delimiter, n) returns everything before the n-th delimiter:
SPECIES = "SUBSTRING_INDEX(organism, ' ', 2)"

with engine.begin() as conn:
    conn.execute(text(f"ALTER TABLE {TABLE} ADD COLUMN proteins_per_gene DOUBLE"))
    conn.execute(text(f"UPDATE {TABLE} SET proteins_per_gene = proteins / genes"))

# print out the answer                                                                            
print("*" * 60)                                                                                   
print()

q5 = query(f"""
    SELECT COUNT(*)                  AS assemblies,
           COUNT(DISTINCT {SPECIES}) AS species
    FROM {TABLE}
    WHERE proteins_per_gene >= 1.1
""")

print()

query(f"""
    SELECT group_name, COUNT(*) AS assemblies
    FROM {TABLE}
    WHERE proteins_per_gene >= 1.1
    GROUP BY group_name
    ORDER BY assemblies DESC
""")

print()

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
print(f"{q5["assemblies"].iloc[0]} assemblies have >= 10% more proteins than genes ({q5["species"].iloc[0]} species)\n")
print()
print("*" * 60)






