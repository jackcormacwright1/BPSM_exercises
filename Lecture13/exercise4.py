#!/bin/python3

#===================================================================

#exercise 4

#Write a Python script/programme which creates nine new 'size range' directories, one for sequences between 100 and 199 bases long, one for sequences between 200 and 299 bases long, etc., etc..
#Choose any one of the .dna files as an input file, and write out each DNA sequence in that input file to a separate file in the appropriate 'size range' directory

#===================================================================

# inputs - dna files, user choice of which one to split
# process
# 1 - get the names of the files in the target directory into a list
# 2 - loop each file
# 3 - if it ends with .dna store it as viable
# 4 - ensure more than 0 files were found
# 5 - for each file check if it was already processed (i.e. a folder already exists)
# 6 - print the files and whether they have been processed
# 7 - ask for input of which one you want to process
# 8 - if it has already been processed ask if you want to overwrite
# 9 - create the directory for the files
# 10 - loop a range from 100 to 1000 stepping by 100 and create the sub folders
# 11 - open the selected dna file and loop the lines
# 12 - calculate the length and floor divide by 100 to get which folder it belongs in
# 13 - open a file for the sequence and write the line
# 14 - output a message about what what processed
# outputs - message to screen, main folder for the input, folders for the sizes, one file per sequence (line) in the correct folder

import os

os.chdir("/home/s1306053/BPSM/exercises/Lecture13")

# Directory containing the original DNA files
directory = "/localdisk/data/BPSM/Lecture13/"

# Find all files ending in .dna
# Create an empty list to store DNA filenames
dna_files = []

# Get all files in the directory
all_files = os.listdir(directory)

# Loop through each file
for filename in all_files:

    # Check whether the filename ends in .dna
    if filename.endswith(".dna"):
    #in case if statements are not allowed yet 
    # dna_files = sorted(directory.glob("*.dna"))

        # Add the filename to our list
        dna_files.append(filename)

# Sort the list alphabetically
dna_files.sort()

# Check that DNA files exist
if len(dna_files) == 0:
    print("No DNA files found.")
    exit()

# Display available DNA files
print("Available DNA files:\n")

for number, filename in enumerate(dna_files, start=1):

    # Check whether an output folder already exists
    folder_name = filename.split(".")[0]

    if os.path.isdir(folder_name):
        status = " (already processed)"
    else:
        status = ""

    print(f"{number}. {filename}{status}")

# Ask the user to choose a file
choice = int(input("\nEnter the number of the file to process: "))

# Check that the selection is valid
if choice < 1 or choice > len(dna_files):
    print("Invalid selection.")
    exit()

# Get the selected filename
filename = dna_files[choice - 1]
input_file = os.path.join(directory, filename)

# Create the output folder name
folder_name = filename.split(".")[0]

# Warn if the output folder already exists
if os.path.isdir(folder_name):

    answer = input(
        f"\nThe folder '{folder_name}' already exists. "
        "Do you want to overwrite existing files? (y/n): "
    )

    if answer.lower() != "y":
        print("Processing cancelled.")
        exit()

# Create the main output directory
os.makedirs(folder_name, exist_ok=True)

# Create nine size-range directories
for size in range(100, 1000, 100):

    folder = f"{size}-{size + 99}"
    folder_path = os.path.join(folder_name, folder)

    os.makedirs(folder_path, exist_ok=True)

# Initialise counters
number = 0
processed = 0

# Open the selected DNA file
with open(input_file, "r") as file:

    for line in file:

        number += 1

        # Remove whitespace and calculate sequence length
        sequence = line.strip()
        length = len(sequence)

        # Determine the correct size range
        # // for floor division 
        lower = (length // 100) * 100
        folder = f"{lower}-{lower + 99}"

        # Construct the output path
        output_folder = os.path.join(folder_name, folder)
        output_filename = f"sequence_{number}.dna"
        output_path = os.path.join(output_folder, output_filename)

        # Write the sequence to its own file
        with open(output_path, "w") as output:
            output.write(sequence + "\n")

        processed += 1

print(f"\nFinished processing {filename}")
print(f"Sequences saved: {processed}")
print(f"Sequences skipped: {number - processed}")
print(f"Output directory: {folder_name}/")


