#
# CS1010S --- Programming Methodology
#
# Sidequest 9.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json
import time

#####################
# Reading json file #
#####################

def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google it :P

    For example, file.txt contains:
    [["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"], ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"], ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]]

    Calling read_json('file.txt') will return the following array
    [
        ["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"],
        ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"],
        ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]
    ]
    """
    datafile = open(filename, 'r', encoding='utf-8')
    return json.loads(datafile.read())

#############
# Accessors #
#############

def module_code(module):
    return module[0]

def module_name(module):
    return module[1]

def module_prof(module):
    return module[2]


###########
# Task 1a #
###########

def merge_lists(all_lst):
    def merge(left, right):
        results = []
        while left and right:
            if left[0] < right[0]:
                results.append(left.pop(0))
            else:
                results.append(right.pop(0))
        results.extend(left)
        results.extend(right)
        return results
    while len(all_lst) > 1:
        merged = merge(all_lst[0],all_lst[1])
        all_lst += [merged]
        all_lst.pop(0)
        all_lst.pop(0)
    return all_lst[0]


all_lst = [[2, 7, 10], [0, 4, 6], [3, 11]]
print("## Q1a ##")
print(merge_lists(all_lst)) # [0, 2, 3, 4, 6, 7, 10, 11]


###########
# Task 1b #
###########

def merge(lists, field):        
    def merge(left, right):
        results = []
        while left and right:
            if field(left[0]) < field(right[0]):
                results.append(left.pop(0))
            else:
                results.append(right.pop(0))
        results.extend(left)
        results.extend(right)
        return results
    while len(lists) > 1:
        merged = merge(lists[0],lists[1])
        lists += [merged]
        lists.pop(0)
        lists.pop(0)
    return lists[0]      


list_of_lists = [[["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"],
                  ["CS3235", "COMPUTER SECURITY", "NORMAN HUGH ANDERSON"]],
                 [["CS4221", "DATABASE DESIGN", "LING TOK WANG"],
                  ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"]]]
print("## Q1b ##")
print(merge(list_of_lists, module_prof))
# [[’CS1010S’, ’PROGRAMMING METHODOLOGY’, ’LEONG WING LUP, BEN’],
#  [’CS4221’, ’DATABASE DESIGN’, ’LING TOK WANG’],
#  [’CS3235’, ’COMPUTER SECURITY’, ’NORMAN HUGH ANDERSON’],
#  [’CS2010’, ’DATA STRUCTURES & ALGORITHMS II’, ’STEVEN HALIM’]

##########
# Task 2 #
##########

def merge_sort(lst, k, field):
    sublists = [lst[x:x+k] for x in range(0,len(lst),k)]
    new_sub = []
    for sublist in sublists:
        new_sub += merge(sublist, field)
    return merge(new_sub,field)
    
        
        


#For your own debugging
modules = read_json('modules_small.txt')
for module in merge_sort(modules, 2, module_code):
    print(module)


########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########

def print_list_to_str(list):
    return '\n'.join(str(x) for x in list)

def test(testfile_prefix):
    print("\n*** Testing with ",testfile_prefix,".txt ***")
    modules = read_json(testfile_prefix+'.txt')
    total_time = 0
    
    modules_sorted_code = open(testfile_prefix+'_sorted_code.txt', 'r', encoding='utf-8').read()
    modules_sorted_name = open(testfile_prefix+'_sorted_name.txt', 'r', encoding='utf-8').read()
    modules_sorted_prof = open(testfile_prefix+'_sorted_prof.txt', 'r', encoding='utf-8').read()
    
    ks = [2,3,5,8,13,21,34,55,89,144]
    pass_k = 0
    
    for k in ks:
        start_time = time.time()
        modules1 = modules.copy()
        modules_answer_code = merge_sort(modules1, k, module_code)
        modules2 = modules.copy()
        modules_answer_name = merge_sort(modules2, k, module_name)
        modules3 = modules.copy()
        modules_answer_prof = merge_sort(modules3, k, module_prof)
        end_time = time.time()
        total_time += (end_time - start_time)
    
        code_same = print_list_to_str(modules_answer_code) == modules_sorted_code
        name_same = print_list_to_str(modules_answer_name) == modules_sorted_name
        prof_same = print_list_to_str(modules_answer_prof) == modules_sorted_prof
        if (code_same and name_same and prof_same):
            pass_k += 1
        print("k = ", k, ", code: ",code_same,", name: ", name_same,", prof: ",prof_same)
    
    print(pass_k,"/", len(ks), " correct! Total time taken: ", total_time, " seconds.")

print("## Q2 ##")
# test('modules_small')
# test('modules')
# test('modules_empty')
