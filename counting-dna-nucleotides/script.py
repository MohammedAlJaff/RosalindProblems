# Counting dna nucleotides

import sys

inFile = sys.argv[1]

with open(inFile) as xfile:

    # returns a list of string-lines
    # Asssumption is that there is only one string in file.
    dna_string_lines = xfile.readlines()
    dna_string = dna_string_lines[0];

    num_a = dna_string.count('A')
    num_g = dna_string.count('G')
    num_t = dna_string.count('T')
    num_c = dna_string.count('C')

    print(num_a, num_c, num_g, num_t)
