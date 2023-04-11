# CS1010S --- Programming Methodology
# Side Quest 11.1 Template

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

#######################
# OPERATION_TABLE ADT #
#######################

OPERATION_TABLE = {}
VALID_TAGS = ('dna', 'rna', 'protein')

def put_op(name, tuple_of_tags_types, operator):
    if name not in OPERATION_TABLE:
        OPERATION_TABLE[name] = {}
    OPERATION_TABLE[name][tuple_of_tags_types] = operator

def get_op(name, tuple_of_tags_types):
    if not all(map(lambda tag_type: tag_type in VALID_TAGS, tuple_of_tags_types)):
        raise Exception('Invalid tag-type(s). Are you sure you are working with Tagged-Data?')
    if name not in OPERATION_TABLE:
        raise Exception(f'Missing operation: {name}. Did you misspell the operation or forget to put_op?')
    if tuple_of_tags_types not in OPERATION_TABLE[name]:
        raise Exception(f'Missing operation for these tags: {tuple_of_tags_types}. Did you forget to put_op?')
    return OPERATION_TABLE[name][tuple_of_tags_types]

#############################
# Functions from Mission 11 #
#############################

# Paste your functions from Mission 11 here!
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

def get_mapping(csvfilename):
    rows = read_csv(csvfilename)[1:]
    diction = {}
    for row in rows:
        diction[row[0]] = row[3]
    return diction

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


##########
# Task 1 #
##########

def tag(tag_type, data):
    return (tag_type,data)

def get_tag_type(obj):
    return obj[0]

def get_data(obj):
    return obj[1]

print("## Q1 ##")
### DO NOT CHANGE THE CODE IN THIS BOX ###
                                         #
### TAGGING DATA ###                     #
dna     = "TTACTCCATATATCGCCGTGCCAT"     #
rna     = transcribe(dna)                #
protein = translate(rna)                 #
tagged_dna     = tag("dna", dna)         #
tagged_rna     = tag("rna", rna)         #
tagged_protein = tag("protein", protein) #
                                         #
### DO NOT CHANGE THE CODE IN THIS BOX ###

print(get_tag_type(tagged_dna))     # 'dna'
print(get_tag_type(tagged_rna))     # 'rna'
print(get_tag_type(tagged_protein)) # 'protein'

print(get_data(tagged_dna) == dna)         # True
print(get_data(tagged_rna) == rna)         # True
print(get_data(tagged_protein) == protein) # True


##########
# Task 2 #
##########

### DO NOT CHANGE THE CODE IN THIS BOX ##################################
                                                                        #
put_op("to_dna", ("dna",), lambda x: x)                                 #
put_op("to_dna", ("rna",), reverse_transcribe)                          #
put_op("to_rna", ("dna",), transcribe)                                  #
put_op("to_rna", ("rna",), lambda x: x)                                 #
put_op("is_same_dogma", ("dna","dna"), lambda x, y: x == y)             #
put_op("is_same_dogma", ("dna","rna"), lambda x, y: transcribe(x) == y) #
put_op("is_same_dogma", ("rna","dna"), lambda x, y: x == transcribe(y)) #
put_op("is_same_dogma", ("rna","rna"), lambda x, y: x == y)             #
                                                                        #
def to_dna(tagged_data):                                                #
    tag_type = get_tag_type(tagged_data)                                #
    data     = get_data(tagged_data)                                    #
    op       = get_op("to_dna", (tag_type,))                            #
    return tag("dna", op(data))                                         #
                                                                        #
### DO NOT CHANGE THE CODE IN THIS BOX ##################################

def to_rna(tagged_data):
    tag_type = get_tag_type(tagged_data)
    data = get_data(tagged_data)
    op = get_op("to_rna", (tag_type,))
    return tag("rna", op(data))

def is_same_dogma(data1, data2):
    if get_tag_type(data1)=="dna":
        some_op = get_op("to_rna", ("dna",))
    else:
        some_op = get_op("to_dna", ("dna",))
    choices = (data1, some_op(data1))
    if data2 in choices:
        return True
    else:
        return False

print("## Q2 ##")
tagged_dna1 = tag("dna", "AAATGC")
tagged_rna1 = tag("rna", "GCAUUU")
tagged_dna2 = tag("dna", "TTACAT")
tagged_rna2 = tag("rna", "AUGUAA")

print(get_data(to_rna(tagged_dna1))) # 'GCAUUU'
print(get_data(to_rna(tagged_rna1))) # 'GCAUUU'

print(is_same_dogma(tagged_dna1, tagged_rna1)) # True
print(is_same_dogma(tagged_rna1, tagged_rna1)) # True
print(is_same_dogma(tagged_rna1, tagged_dna2)) # False

##########
# Task 3 #
##########

# (a)
def to_protein(*your_args_here):
    """Your code here"""


# (b)
put_op("""your_args_here""") # converts Tagged-DNA to Tagged-Protein
put_op("""your_args_here""") # converts Tagged-RNA to Tagged-Protein
put_op("""your_args_here""") # converts Tagged-Protein to Tagged-Protein


# (c)
put_op("""your_args_here""") # checks Tagged-Protein/Tagged-Protein
put_op("""your_args_here""") # checks Tagged-Protein/Tagged-DNA
put_op("""your_args_here""") # checks Tagged-DNA/Tagged-Protein
put_op("""your_args_here""") # checks Tagged-Protein/Tagged-RNA
put_op("""your_args_here""") # checks Tagged-RNA/Tagged-Protein


# (d)
#dna_1 = to_dna(protein)
#dna_2 = to_dna(to_protein(tagged_rna))
#dna_3 = to_dna(tagged_rna)
#dna_4 = to_dna(tagged_protein)
#dna_5 = to_dna(to_protein(tagged_dna))
#dna_6 = to_dna(to_rna(tagged_dna))
#dna_7 = to_dna(to_rna(tagged_protein))
#dna_8 = to_dna(to_protein(to_rna(tagged_dna)))
#dna_9 = to_dna(to_rna(to_protein(dna_1)))
#dna_10 = ('dna', get_data(dna_6))


# (e)
# Give 6 examples of Tagged-RNAs that will give rise to the Tagged-Protein with data "MYVHAN_"
my_rna_list = []


# (f)
# Number of Tagged-RNAs that will give rise to the Tagged-Protein with data "MYVHAN_"
num_rnas = "" # replace with your answer
