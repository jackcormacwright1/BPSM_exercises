#!/usr/bin/env python3
# Exercise 2

################################################################################################

#Modify the function from the previous exercise above so that it accepts a list of amino acid 
#residues rather than a single one, and count these within the protein sequence.
#If no list is given, the function should return the percentage of hydrophobic amino acid residues 
#(i.e. amino acids A, I, L, M, F, W, Y, V).

#Your function should pass the following assertions:
#assert round(some_other_function_name("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
#assert round(some_other_function_name("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
#assert round(some_other_function_name("MSRSLLLRFLLFLLLLPPLP")) == 65

#Hint: To get this one to work, you'll have to go through the list of amino acid residues 
#one at a time, generate the count for each one, and come up with a total count.

################################################################################################


def amino_acid_percentages(protein, residues=["A", "I", "L", "M", "F", "W", "Y", "V"]):
    protein = protein.upper()
    if len(protein) == 0:
        raise ValueError("The protein sequence is empty!!!!!!!")

    total = 0
    counted = []
    for residue in residues:
        residue = residue.upper()
        # Count each residue only once even if repeated in the input
        if residue not in counted:
            total = total + protein.count(residue)
            counted.append(residue)

    return total / len(protein) * 100






if __name__ == "__main__":
    assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
    assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP", ["F", "S", "L"])) == 70
    assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP")) == 65

    print("Tests completed")
    print("Hydrophobic percentage:", amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP"))











