#!/bin/python3

import subprocess, os

os.chdir("/home/s1306053/BPSM/exercises/Lecture12")

database = "/home/s1306053/BPSM/exercises/Lecture06/nem"

files = [
    "AJ223353.1_coding.fasta",
    "AJ223353.1_noncoding.fasta",
    "plain_sequence_coding.fasta",
    "plain_sequence_noncoding.fasta",
]

for filename in files:
    output = filename.replace(".fasta", "_blast.txt")

    print()
    print("=" * 60)
    print(f"Running BLAST on: {filename}", flush=True)

    subprocess.run([
        "blastx",
        "-query", filename,
        "-db", database,
        "-out", output,
        "-outfmt", "7",
    ], check=True)

    print("\nResults saved to", output)

    with open(output, "r") as file:
        results = file.read()

    # Split the output into one part per query sequence 
    # using the query identifier from the header comments as delimiter
    # Skip the text before the first query by slicing the list starting at 1
    # i.e. remove the first section at the 0 index
    query_sections = results.split("# Query:")[1:]

    for section in query_sections:

        print()
        print("-" * 20)

        # The query name is on the first line.
        name_end = section.find("\n")
        query_name = section[:name_end]

        print(f"Sequence: {query_name}")

        if "# 0 hits found" in section:
            print("No hits found.")

        else:
            # The results start afte the "hits found" comment line.
            hits_position = section.find(" hits found")
            # look for the first newline after the hits found comment
            # then plus 1 to move on to the next line, i.e. the start of the results
            result_start = section.find("\n", hits_position) + 1
            # get the results for this section which are from the line
            # where the resuls start to the end of the section
            remaining_results = section[result_start:]
            # split it on a new line delimiter and take the 0th line i.e. first i.e. top hit
            top_hit = remaining_results.split("\n")[0]

            # BLAST separates the result columns with tabs.
            columns = top_hit.split("\t")

            print(f"Top reported hit: {columns[1]}")
            print(f"Percentage identity: {columns[2]}%")
            print(f"E-value: {columns[10]}")
            print(f"Bit score: {columns[11]}")

    
print()
print("=" * 60)
print("All searches finished.")



























