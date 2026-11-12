#!/usr/bin/env python3
# Exercise 1

################################################################################

#Write a Python function that takes two arguments (a protein sequence and an amino acid residue code) 
#and returns the percentage of the protein that the amino acid makes up.

#Once you have written a function, use the following assertions to test your function:
#assert round(some_function_name("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
#assert round(some_function_name("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
#assert round(some_function_name("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
#assert round(some_function_name("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)

################################################################################


def amino_acid_percentage(protein, residue):
    # Convert both strings to uppercase
    protein = protein.upper()
    residue = residue.upper()

    # Flag empty protein string as error
    if len(protein) == 0:
        raise ValueError("The protein sequence is empty!!!")

    # Divide residue count by total length then convert to percent with x100
    count = protein.count(residue)
    return count / len(protein) * 100




if __name__ == "__main__":
    assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "M")) == 5
    assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "r")) == 10
    assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "L")) == 50
    assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "Y")) == 0

    print("Tests complete")

    print("Percentage of L:", amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "L"))

