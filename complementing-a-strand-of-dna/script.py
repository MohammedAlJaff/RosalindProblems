

s = 'TCAATAACATCGTATCTACTGATTACGTACTTACGTTGGAGAGAAACCCAAACCTTTTTCCGGATGCGTTTGAGGACAATGAACACCGCGTCGTATCCACACTTCCTTTTTTGGGACAATTTCATGTGTCGTTCTACAAGATATGCTAAGTTTTTTAGTTCCCTCGGGGCTACAAAGCTGAGTCTCTAGCATCCTACCCGAACCAGTGCCGTAAAATAAGTGTATTAGATGTGTTGTCTTGCAATCAGGGCGACGCGTATTCCCGCCTGAGTGTCGACACCGATCACCGCATGTATTACCTACGTCCTCCTGCTAGTCTAGCGAATGCAAGATAGTATAAGCTAGTACTTAGACGTAGCGCTCTCCCGTCAGGGACCCTCCCGCGCACATGATTACCGCTGGCACCGTATAAACCATATGAGTGGCGCGTGGCCTACAGCTATAGCTAAGTTCCAGATGCTTGCAGAACTTGACTAGAGTAATAACCCCCAAGGTTCCACTTTCTGACAGCCATACTGCCATTCGATAGCGCCGCGACTATCTACTTGAAGCTCACATTAACCGGAGCGGGCGTTTCTATATAGACAATACTGGTTAGGAGCCTCTGATCGCAACAACCCTGACGCCGCGGTTCAGTCACTAGGGTATCCCGACGCGTAAAAGGAGTTGAAAGATCTACCACGTGGGTTAAAGGCATTCACGTGTTGCACTGTCCATCCTTCAATGAATGTGCATCCACTAATTTGGAGTCCTAGGAGATTGGAGTGCTATTGGATTTTTCGCTGAAAGATGCAAAAGTACGGCAGGTTATTTGAAGGCTCGGTCCATAAC'

def reverse_complement1(dna_string):

    rev_comp = '';
    for indx in range(len(dna_string)-1,-1, -1):

        if dna_string[indx] == 'A':
            rev_comp += 'T'

        elif dna_string[indx] == 'T':
            rev_comp += 'A'

        elif dna_string[indx] == 'C':
            rev_comp += 'G'

        elif dna_string[indx] == 'G':
            rev_comp += 'C'


    return rev_comp


# Alt solution cool and more elegant solution (not mine)
def reverse_complement2(dna_string):
    trans_table = str.maketrans('ATGC', 'TACG')
    return dna_string[::-1].translate(trans_table)


new_s1 = reverse_complement1(s)
new_s2 = reverse_complement2(s)


print(new_s1)
print(new_s2)
