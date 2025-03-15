# David Jo. Assignment 5 "Trees and Dictionaries" Part 2
# Program prupose: To implement a dictionary that will output amino acids given a nucleotide sequence

def print_amino_acids():
    nucleotides_dict = {
        'TTT': 'Phe',
        'TTC': 'Phe',
        'TTG': 'Leu',
        'TTA': 'Leu',
        'TCT': 'Ser',
        'TCC': 'Ser',
        'TCG': 'Ser',
        'TCA': 'Ser',
        'TGT': 'Cys',
        'TGC': 'Cys',
        'TGG': 'Trp',
        'TGA': '***',
        'TAT': 'Tyr',
        'TAC': 'Tyr',
        'TAG': '***',
        'TAA': '***',
        'CTT': 'Leu',
        'CTC': 'Leu',
        'CTG': 'Leu',
        'CTA': 'Leu',
        'CCT': 'Pro',
        'CCC': 'Pro',
        'CCG': 'Pro',
        'CCA': 'Pro',
        'CGT': 'Arg',
        'CGC': 'Arg',
        'CGG': 'Arg',
        'CGA': 'Arg',
        'CAT': 'His',
        'CAC': 'His',
        'CAG': 'Gln',
        'CAA': 'Gln',
        'GTT': 'Val',
        'GTC': 'Val',
        'GTG': 'Val',
        'GTA': 'Val',
        'GCT': 'Ala',
        'GCC': 'Ala',
        'GCG': 'Ala',
        'GCA': 'Ala',
        'GGT': 'Gly',
        'GGC': 'Gly',
        'GGG': 'Gly',
        'GGA': 'Gly',
        'GAT': 'Asp',
        'GAC': 'Asp',
        'GAG': 'Glu',
        'GAA': 'Glu',
        'ATT': 'Ile',
        'ATC': 'Ile',
        'ATG': 'Met',
        'ATA': 'Ile',
        'ACT': 'Thr',
        'ACC': 'Thr',
        'ACG': 'Thr',
        'ACA': 'Thr',
        'AGT': 'Ser',
        'AGC': 'Ser',
        'AGG': 'Arg',
        'AGA': 'Arg',
        'AAT': 'Asn',
        'AAC': 'Asn',
        'AAG': 'Lys',
        'AAA': 'Lys'
        }
        
    while True:
        nucleotide_sequence = str(input("Enter a nucleotide sequence, or just press ENTER to quit: ")).replace(" ", "")

        if not nucleotide_sequence:
            break
        
        # I know you said to make a clean_sequence function but I really like list comprehensions and this seemed cleaner to me? I think it's more efficient? I might be wrong though...
        # But this returns a string of only the alphabetic characters and all as uppercase
        only_letters_sequence = "".join([nucleotide_sequence[i].upper() for i in range(len(nucleotide_sequence)) if nucleotide_sequence[i].isalpha()])
        if len(only_letters_sequence) % 3 != 0:
            print("Error: You must give complete triples.")
            print()
            continue

        # This cuts that cleaned string into triples
        triplets = [str(only_letters_sequence[i:i+3]) for i in range(0, len(only_letters_sequence), 3)]

        # This is where we actually use the dictionary to output the corresponding amino acid
        for triple in triplets: 
            if (triple in nucleotides_dict.keys()):
                print(f"{triple} {nucleotides_dict[triple]}")
            else:
                print(f"{triple} invalid sequence")
        print()


def main():
    print_amino_acids()


if __name__ == '__main__':
    main()