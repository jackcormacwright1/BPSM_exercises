#!/bin/python3

#==============================================================

#exercise 3

# 1 write a Python programme that generates segments that are 30 bases long, with a window offset of 3.
# 2 Modify your Python script/programme to print each sliding window segment to the screen.
# 3 Modify your Python script/programme to print the percentage GC content of each sliding window segment and the sequence.
# 4 Modify your Python script/programme to write out the individual segments in fasta format (i.e. with an informative fasta header) into individual fasta files.
# 5 Modify your Python script/programme to write out the individual segments in fasta format (i.e. with an informative fasta header) into a single fasta file.
# 6 Modify your Python script/programme to include the partial sliding window segments that we get at the end of the sequence

#===============================================================

# inputs - dna sequence from previous lecture, output directory path, window size, step size
# process
# 1 - create the output directory
# 2 - read in the fasta
# 3 - open a new file to take the combined output
# 4 - loop a range from 0 to the dna length counting up by the step size
# 5 - slice the dna at the start positions to start + window length
# 6 - calculate gc percentage
# 7 - create fasta header for the window
# 8 - print the sequence and gc content
# 9 - write the header and segment to an individual file
# 10 - write the header and segment to the combined file
# loop
# outputs - message to the screen, individual files, combined file, folder

import os

# Set output directory as this will produce a lot of files
outputdir = "/home/s1306053/BPSM/exercises/Lecture13/exercise3_outputs"
os.makedirs(outputdir, exist_ok=True)

# Read DNA sequence
with open("/home/s1306053/BPSM/exercises/Lecture12/AJ223353.1_coding1.fasta", "r") as file:
    file.readline()
    dna = file.read()

window_size = 30
step_size = 3

# Open a single FASTA output file
with open(os.path.join(outputdir, "all_windows.fasta"), "w") as combined_file:

    for start in range(0, len(dna), step_size):

        # Extract segment (including partial windows)
        segment = dna[start:start + window_size]

        # Calculate GC percentage
        gc = (segment.count("G") + segment.count("C")) / len(segment) * 100

        # Create informative FASTA header
        header = f">window_{start + 1}_to_{start + len(segment)}_GC_{gc:.2f}%"

        # Print sequence and GC content
        print(header)
        print(segment)

        # Write individual FASTA file
        filename = f"window_{start + 1}.fasta"
        filepath = os.path.join(outputdir, filename)

        with open(filepath, "w") as individual_file:
            individual_file.write(header + "\n")
            individual_file.write(segment + "\n")

        # Write to combined FASTA file
        combined_file.write(header + "\n")
        combined_file.write(segment + "\n")



