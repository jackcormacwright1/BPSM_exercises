#!/bin/python3

#==========================================================

# exercise 1

#The file input.txt contains a number of DNA sequences, one per line.
#Each sequence starts with the same 14 base pairs : these are from a sequencing adapter that should have been removed.

#Write a Python script/programme that will :
#(a) trim the adapter and write the 'cleaned' (adapter-free) sequences to a single new file AND
#(b) print the length of each adapter-free sequence to the screen.

#==========================================================

# inputs - input.txt file, 14 chars in the adapter
# process
# 1 - open the input file
# 2 - loop each sequence (line)
# 3 - trim the sequence
# 4 - append to a list
# 5 - calculate and print length
# 6 - close the file
# 7 - open a new file for the trimmed sequences
# 8 - loop the list and write
# 9 - close the file
# outputs - a file with the trimmed sequences



# Initialise a counter and an empty list to store trimmed sequences
count = 0
trimmed_sequences = list()

# Open the input file containing the DNA sequences
my_file = open("Lecture13/input.txt")

# Loop through each sequence in the file
for line in my_file:
    count += 1

    # Remove the newline character and trim the first 14 bases
    # Index starts at 0 so 14 will give the 15th character onwards
    trimmed_sequence = line.rstrip('\n')[14:]

    # Add the trimmed sequence to the list, with a newline character
    trimmed_sequences.append(trimmed_sequence + '\n')

    # Calculate and print the length of the adapter-free sequence
    line_length = len(trimmed_sequence)
    print(f'Sequence {count}: {line_length} bases')

# Close the input file
my_file.close()

# Open a new file to write the trimmed sequences
write_my_file = open("1_trimmed_sequences.txt", "w")

# Loop through the list and write each trimmed sequence to the output file
for line in trimmed_sequences:
    write_my_file.write(line)

# Close the output file
write_my_file.close()
