# CS1010S --- Programming Methodology
# Mission 11 Template

# Note that written answers are stored in """multi-line strings"""
# to allow us to run your code easily when grading your problem set.

import csv

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows


##########
# Task 1 #
##########

def replicate(dna_strand):
    dna_base_pairings = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    result = ""
    for i in range(len(dna_strand)):
        key = dna_strand[i]
        result += dna_base_pairings[key]
    return result[::-1]

print("## Q1 ##")
print(replicate("AAATGC"))     # 'GCATTT'
print(replicate("ATTGGGCCCC")) # 'GGGGCCCAAT'

with open("dna.txt") as f:
    dna = f.read()
print(replicate(dna )[:10])    #'AATAGTTTCT'


##########
# Task 2 #
##########

def transcribe(dna_strand):
    dna_base_pairings = {
        "A": "U",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    result = ""
    for i in range(len(dna_strand)):
        key = dna_strand[i]
        result += dna_base_pairings[key]
    return result[::-1]

def reverse_transcribe(rna_strand):
    rna_base_pairings = {
        "A": "T",
        "U": "A",
        "G": "C",
        "C": "G"
    }
    result = ""
    for i in range(len(rna_strand)):
        key = rna_strand[i]
        result += rna_base_pairings[key]
    return result[::-1]

print("## Q2 ##")
print(transcribe("AAATGC"))     # 'GCAUUU'
print(transcribe("ATTGGGCCCC")) # 'GGGGCCCAAU'

print(reverse_transcribe(transcribe("AAATGC"))) # 'AAATGC'
print(reverse_transcribe("GGGGCCCAAU"))         # 'ATTGGGCCCC'

rna = transcribe(dna)
print(rna[-10:])                # 'GAAUAUGUGA'


##########
# Task 3 #
##########

def get_mapping(csvfilename):
    rows = read_csv(csvfilename)[1:]
    diction = {}
    for row in rows:
        diction[row[0]] = row[3]
    return diction

print("## Q3 ##")
codon2amino = get_mapping("codon_mapping.csv")

print(codon2amino["ACA"]) # 'T'
print(codon2amino["AUU"]) # 'I'
print(codon2amino["CUC"]) # 'L'
print(codon2amino["ACU"]) # 'T'
print(codon2amino["UAG"]) # '_'
print(codon2amino["UGA"]) # '_'


##########
# Task 4 #
##########

def translate(rna_strand):
    codon2amino = get_mapping("codon_mapping.csv")
    if "AUG" not in rna_strand:
        return None
    if "UAA" not in rna_strand and "UAG" not in rna_strand and "UGA" not in rna_strand:
        return None
    else:
        result = ""
        for i in range(len(rna_strand)-2):
            if rna_strand[i:i+3] == "AUG":
                behind = rna_strand[i:]
                break
        for i in range(0,len(behind), 3):
            key = behind[i:i+3]
            if key in codon2amino:
                result += codon2amino[key]
                if codon2amino[key] == "_":
                    break
                else:
                    continue
            else:
                break
        return result
    

print("## Q4 ##")
print(translate("AUGUAA"))           # 'M_'
print(translate("AGAGAUGCCCUGAGGG")) # 'MP_'

protein = translate(rna)
print(protein) # 'MANLTNFHLKIYIHTYIQLKHLSSGAFSLFSAHNSRSINYNYYFSFRDLNITYNHTHLTTY_'
print(protein == 'MANLTNFHLKIYIHTYIQLKHLSSGAFSLFSAHNSRSINYNYYFSFRDLNITYNHTHLTTY_') # True


##########
# Task 5 #
##########

'''
=== Space Complexity Analysis ===
to create get_mapping (dict): O(...)
to create get_mapping (list): O(...)

=== Time Complexity Analysis ===
codon lookup using codon2amino (dict): O(...)
codon lookup using codon2amino (list): O(...)

=== Conclusion ===
State and justify which is the better implementation.
Answer here.
'''
