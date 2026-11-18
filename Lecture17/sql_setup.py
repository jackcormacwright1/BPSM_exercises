import os

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

file_path = "eukaryotes.txt"

MYSQL_USER = "s1306053"
MYSQL_DB = "s1306053_PandaPlay"
MYSQL_HOST = "129.215.237.85"
TABLE = "eukaryotes"

password = os.environ.get("MySQL_password")

################################################################################
# 1. Read the file into pandas
################################################################################

df = pd.read_csv(file_path, sep="\t", na_values="-")

# Rename the columns
df = df.rename(columns={
    "#Organism/Name": "organism",
    "TaxID": "taxid",
    "BioProject Accession": "bioproject_accession",
    "BioProject ID": "bioproject_id",
    "Group": "group_name",
    "SubGroup": "subgroup",
    "Size (Mb)": "size_mb",
    "GC%": "gc_pct",
    "Assembly Accession": "assembly_accession",
    "Replicons": "replicons",
    "WGS": "wgs",
    "Scaffolds": "scaffolds",
    "Genes": "genes",
    "Proteins": "proteins",
    "Release Date": "release_date",
    "Modify Date": "modify_date",
    "Status": "status",
    "Center": "center",
    "BioSample Accession": "biosample_accession",
})

print(f"Read {file_path}: {len(df):,} rows")


################################################################################
# 2. Connect to MySQL and write the dataframe into a table
################################################################################

url = URL.create("mysql+mysqldb", 
                 username=MYSQL_USER, 
                 password=password,
                 host=MYSQL_HOST, 
                 database=MYSQL_DB
                 )

engine = create_engine(url)

# if_exists="replace" to drop any old copy first, so the script can be re-run
# index=False means don't write pandas' 0,1,2... row index as an extra column
# chunksize=5000 means send rows in INSERT batches of 5000 rather than all at once
# NaN values become SQL NULL.
df.to_sql(
        name=TABLE,
        con=engine, 
        if_exists="replace", 
        index=False, 
        chunksize=5000
        )
print(f"Wrote table {MYSQL_DB}.{TABLE}\n")


