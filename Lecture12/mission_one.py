#!/bin/python3

#download these files before running
# efetch -db nucleotide -id AJ223353.1 -format fasta > AJ223353.fasta
# efetch -db nucleotide -id AJ223353.1 -format gb > AJ223353.gb

#and copy across the plain sequence file to the current directory
#cp /localdisk/data/BPSM/Lecture12/plain_genomic_seq.txt .

###############################################################################
# Read the input files
###############################################################################

remote_accession = "AJ223353.1"
local_accession = "plain_sequence"

gb_path = "/localdisk/home/s1306053/BPSM/BPSM12/AJ223353.gb"
with open(gb_path, "r") as file:
    gb_contents = file.read()

fasta_path = "/localdisk/home/s1306053/BPSM/BPSM12/AJ223353.fasta"
with open(fasta_path, "r") as file:
    fasta_contents = file.read()

plain_seq_path = "/localdisk/home/s1306053/BPSM/BPSM12/plain_genomic_seq.txt"
with open(plain_seq_path, "r") as file:
    plain_seq_contents = file.read()

###############################################################################
# Remove the remote FASTA header and clean both sequences
###############################################################################

header_end = fasta_contents.find("\n")
remote_sequence = fasta_contents[header_end + 1:]

# Remove whitespace and convert to uppercase.
# Keep Xs and other non-ATCG characters so coordinates do not shift.
remote_sequence = "".join(remote_sequence.split()).upper()
local_sequence = "".join(plain_seq_contents.split()).upper()

###############################################################################
# Check the sequence characters
###############################################################################

for name, sequence in [
    (remote_accession, remote_sequence),
    (local_accession, local_sequence),
]:
    print(f"\nChecking sequence characters: {name}")

    total_bases = len(sequence)
    valid_bases = (
        sequence.count("A")
        + sequence.count("T")
        + sequence.count("C")
        + sequence.count("G")
    )

    other_bases = total_bases - valid_bases

    print(f"Total characters: {total_bases}")
    print(f"A, T, C or G: {valid_bases}")
    print(f"Characters other than A, T, C or G: {other_bases}")
    print(f"Percentage other than A, T, C or G: {other_bases / total_bases:.2%}")
    print(f"Number of U characters: {sequence.count('U')}")
    print(f"Number of X characters: {sequence.count('X')}")

###############################################################################
# Read the remote molecule type from the GenBank annotations
###############################################################################

marker = '/mol_type="'
remote_type_start = gb_contents.find(marker)
remote_type_start = remote_type_start + len(marker)
remote_type_end = gb_contents.find('"', remote_type_start)
molecule_type = gb_contents[remote_type_start:remote_type_end]

print(f"\nRemote molecule type: {molecule_type}")

# AJ223353 is annotated as mRNA, represented using T rather than U.
# Using this accession because it is requested by the exercise
# although the instructions only refer to genomic DNA

###############################################################################
# Find the remote CDS coordinates
###############################################################################

cds_marker = "     CDS             "
cds_index = gb_contents.find(cds_marker)
line_end = gb_contents.find("\n", cds_index)
location = "".join(gb_contents[cds_index + len(cds_marker):line_end].split())
separator = location.find("..")
start_text = location[:separator]
end_text = location[separator + 2:]
remote_coding_start = int(start_text)
remote_coding_end = int(end_text)

###############################################################################
# Define the local coding coordinates
###############################################################################

# These coordinates start at 1 and include both endpoints.
local_coding_start1 = 1
local_coding_end1 = 63

local_coding_start2 = 91
local_coding_end2 = len(local_sequence)

###############################################################################
# Extract coding and non-coding regions
###############################################################################

# Python starts counting at 0 and excludes the slice endpoint.
# Inclusive biological coordinates start..end become [start - 1:end].

remote_coding_seq1 = remote_sequence[remote_coding_start - 1:remote_coding_end]

local_coding_seq1 = local_sequence[local_coding_start1 - 1:local_coding_end1]

local_coding_seq2 = local_sequence[local_coding_start2 - 1:local_coding_end2]

# Extract the regions outside the coding intervals.
remote_non_coding_seq1 = remote_sequence[:remote_coding_start - 1]
remote_non_coding_seq2 = remote_sequence[remote_coding_end:]

local_non_coding_seq1 = local_sequence[local_coding_end1:local_coding_start2 - 1]

###############################################################################
# Create unique identifiers and FASTA headers
###############################################################################

remote_coding_id1 = remote_accession + "_coding1"
remote_non_coding_id1 = remote_accession + "_noncoding1"
remote_non_coding_id2 = remote_accession + "_noncoding2"

local_coding_id1 = local_accession + "_coding1"
local_coding_id2 = local_accession + "_coding2"
local_non_coding_id1 = local_accession + "_noncoding1"

remote_coding_head1 = f">{remote_coding_id1} length:{len(remote_coding_seq1)}"
remote_non_coding_head1 = f">{remote_non_coding_id1} length:{len(remote_non_coding_seq1)}"
remote_non_coding_head2 = f">{remote_non_coding_id2} length:{len(remote_non_coding_seq2)}"

local_coding_head1 = f">{local_coding_id1} length:{len(local_coding_seq1)}"
local_coding_head2 = f">{local_coding_id2} length:{len(local_coding_seq2)}"
local_non_coding_head1 = f">{local_non_coding_id1} length:{len(local_non_coding_seq1)}"

###############################################################################
# Write one FASTA file for each region
###############################################################################

individual_records = [
    (remote_coding_id1, remote_coding_head1, remote_coding_seq1),
    (remote_non_coding_id1, remote_non_coding_head1, remote_non_coding_seq1),
    (remote_non_coding_id2, remote_non_coding_head2, remote_non_coding_seq2),
    (local_coding_id1, local_coding_head1, local_coding_seq1),
    (local_coding_id2, local_coding_head2, local_coding_seq2),
    (local_non_coding_id1, local_non_coding_head1, local_non_coding_seq1),
]

for identifier, header, sequence in individual_records:
    with open(identifier + ".fasta", "w") as my_file:
        my_file.write(header + "\n")
        my_file.write(sequence + "\n")

###############################################################################
# Write combined coding and non-coding FASTA files for each input
###############################################################################

with open(remote_accession + "_coding.fasta", "w") as my_file:
    my_file.write(remote_coding_head1 + "\n")
    my_file.write(remote_coding_seq1 + "\n")

with open(remote_accession + "_noncoding.fasta", "w") as my_file:
    my_file.write(remote_non_coding_head1 + "\n")
    my_file.write(remote_non_coding_seq1 + "\n")
    my_file.write(remote_non_coding_head2 + "\n")
    my_file.write(remote_non_coding_seq2 + "\n")

with open(local_accession + "_coding.fasta", "w") as my_file:
    my_file.write(local_coding_head1 + "\n")
    my_file.write(local_coding_seq1 + "\n")
    my_file.write(local_coding_head2 + "\n")
    my_file.write(local_coding_seq2 + "\n")

with open(local_accession + "_noncoding.fasta", "w") as my_file:
    my_file.write(local_non_coding_head1 + "\n")
    my_file.write(local_non_coding_seq1 + "\n")

###############################################################################
# Print a summary
###############################################################################

print("\nRemote sequence")
print(f"Total length: {len(remote_sequence)}")
print(f"CDS coordinates: {remote_coding_start}–{remote_coding_end}")
print(f"Coding length: {len(remote_coding_seq1)}")
print(f"Non-coding region 1 length: {len(remote_non_coding_seq1)}")
print(f"Non-coding region 2 length: {len(remote_non_coding_seq2)}")

print("\nLocal sequence")
print(f"Total length: {len(local_sequence)}")
print(f"Coding region 1: {local_coding_start1}–{local_coding_end1}")
print(f"Coding region 2: {local_coding_start2}–{local_coding_end2}")
print(f"Coding region 1 length: {len(local_coding_seq1)}")
print(f"Coding region 2 length: {len(local_coding_seq2)}")
print(f"Non-coding region length: {len(local_non_coding_seq1)}")




