#!/bin/python3                                                                

#===============================================================              

# exercise 2                                                                  

# The file genomic_dna2.txt contains a section of genomic DNA.                
# The file exons.txt contains a list of start/stop positions of exons.        
# Each exon is on a separate line and the start and stop positions are separated by a comma.                                                                

# Write a Python script/programme that will extract the exon segments, concatenate them, and write them to a new file.                                      

#================================================================             

# Read the genomic DNA sequence                                               
with open("Lecture13/genomic_dna2.txt", "r") as file:                       
    dna = file.read()                                       

# Create an empty string for the combined exons                               
exon_dna = ""                                                                 

# Read the exon positions                                                     
with open("Lecture13/exons.txt", "r") as file:                                          

    for line in file:                                                         
        
        start, stop = line.split(",")                                 
    
        # Convert positions to integers                                       
        start = int(start)                                                    
        stop = int(stop)                                                      
        
        # Extract and concatenate the exon                                    
        exon_dna += dna[start - 1:stop]                                       

# Write the combined exon sequence to a new file                              
with open("2_extracted_exons.txt", "w") as file:                                
    file.write(exon_dna)                                                      

print("Exons extracted successfully.\nFirst 100 characters:") 

with open("2_extracted_exons.txt") as file:
    print(file.read()[:100])


