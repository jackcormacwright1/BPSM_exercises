#!/bin/python3

################################################################################

# exercise 1

# Write a Python programme/script that will print only the accessions that 
# satisfy the following criteria individually (i.e. treat each criterion separately)

################################################################################

import re

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp','hsdfusku3345']

regex_criteria = [
('contain the number 5',                                                            r'5'),
('contain the letter d or e',                                                       r'[de]'),
('contain the letters d and e in that order',                                       r'd.*e'),
('contain the letters d and e in that order with a single letter between them',     r'd[a-z]e'),
('contain both the letters d and e in any order',                                   r'd.*e|e.*d'),
('start with x or y',                                                               r'^[xy]'),
('start with x or y and end with e',                                                r'^[xy].*e$'),
('contains any 3 numbers in any order',                                             r'\d.*\d.*\d'),
('contains 3 different numbers in the accession',                                   r'(\d).*(?!\1)(\d).*(?!\1|\2)\d'),
('contain three or more numbers in a row',                                          r'\d{3,}'),
('end with d followed by either a, r or p',                                         r'd[arp]$')
]

print('*' * 60)
print('Testing regex criteria against a list of accession IDs:\n')
print('Accession IDs being tested:\n')

for i, accession in enumerate(accessions):
    print(i, ' ', accession)

for criterion, regex in regex_criteria:
    print('-' * 30)
    print(criterion, ':')
    for i, accession in enumerate(accessions):
        if re.search(regex, accession):
            print(i, ' ', accession)
    
print('-' * 30)

print('ALTERNATIVE METHOD:', 'contains 3 different numbers in the accession')
for i, accession in enumerate(accessions):
    digits = re.findall(r'\d', accession)
    if len(set(digits)) >= 3:
        print(i, ' ', accession)

print()
print('*' * 60)







