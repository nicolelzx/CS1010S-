# CS1010S --- Programming Methodology
# Mission 15 Template

import csv
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

###############
# Pre-defined #
###############

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename, 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

##########
# Task 1 #
##########

def clean(data):
    data = tuple(filter(lambda x: "" not in x, data))
    num = {} #dict of studentno:index
    for i in range(len(data)):
        row = data[i]
        if row[0] not in num.keys():
            num[row[0]] = i
        else:
            if row[6] > data[ num[row[0]] ][6]:
                del num[row[0]]
                num[row[0]] = i
            else:
                continue
    new_data = ()
    for i in num.values():
        row = data[i]
        if row[8]=='yes':
            afast = True
        elif row[8]=="no":
            afast = False
        else:
            afast = None
        new_data += ((str(row[0]),int(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),str(row[7]),afast),)
    return new_data
        
# Do not modify, required for later tasks
raw_data = read_csv("cs1010s.csv")
headers = raw_data[0]
data = clean(raw_data[1:])

# Task 1 Testcase
print(headers)
print(data[:3])

##########
# Task 2 #
##########

def value_counts(data, headers, col_name):
    for i in range(len(headers)):
        if headers[i] == col_name:
            index = i
            break
        else:
            continue
    count = {}
    for row in data:
        option = row[index]
        if option not in count:
            count[option] = 1
        else:
            count[option] += 1
    count = list( [option,num] for num, option in count.items() )
    count.sort(reverse=True)
    cat = []
    num = []
    for x in count:
        num.append(x[0])
        cat.append(x[1])
    return (cat,num)

afast_counts = value_counts(data, headers, "is_afast")
faculty_counts = value_counts(data, headers, "faculty")

# Task 2 Testcases
sns.barplot(x=afast_counts[0], y=afast_counts[1])
plt.title("AFAST Count")
#plt.show() # uncomment to show
plt.close()

sns.barplot(x=faculty_counts[0], y=faculty_counts[1])
plt.title("Number of students from each faculty")
plt.xticks(rotation=90)
#plt.show() # uncomment to show
plt.close()

##########
# Task 3 #
##########

def long2wide(data, headers):
    new = [ [],[],[],[],[],[],[],[],[] ]
    for row in data:
        for i in range(len(headers)):
            new[i].append(row[i])
    result = {}
    for i in range(len(headers)):
        result[headers[i]] = new[i]
    return result
    

# Do not modify, required for later tasks
wide_data = long2wide(data, headers)

# Task 3 Testcases
print(long2wide([["apple", "red"],["banana", "yellow"],["banana", "green"],["apple", "green"],["cherry", "red"]], ["fruit", "colour"]))
# {'fruit': ['apple', 'banana', 'banana', 'apple', 'cherry'], 'colour': ['red', 'yellow', 'green', 'green', 'red']}

sns.histplot(data=wide_data , x="midterm")
plt.title("Midterm Distribution (default)")
#plt.show() # uncomment to show
plt.close()

##########
# Task 4 #
##########

# 4A
def bin_sqrt(values):
    return math.ceil((len(values))**0.5)

# 4B
def bin_rice(values):
    return 2* math.ceil((len(values))**(1/3))

# 4C
def bin_sturge(values):
    return 1 + math.ceil(np.log(len(values))//np.log(2))

# 4D
def bin_scott(values):
    a = math.ceil((len(values))**(1/3))
    b = (max(values)-min(values)) / (3.49*np.std(values, ddof=1))
    return a*b

# 4E
def bin_fd(values):
    a = (max(values)-min(values))/2
    b = ( np.percentile(values,75) - np.percentile(values,25))**(1/3)
    return math.ceil(a*b)

# Task 4 Testcases
print(bin_sqrt(wide_data['midterm']))   # 46
print(bin_rice(wide_data['midterm']))   # 26
print(bin_sturge(wide_data['midterm'])) # 12
print(bin_scott(wide_data['midterm']))  # 19
print(bin_fd(wide_data['midterm']))     # 98

fig, axes = plt.subplots(2, 3, sharex=True, figsize=(15, 5))
fig.suptitle('Midterm Distribution (various bin strategies)')
sns.histplot(ax=axes[0,0], data=wide_data, x="midterm")
axes[0,0].set_title('default')
sns.histplot(ax=axes[0,1], data=wide_data, x="midterm", bins=bin_sqrt(wide_data["midterm"]))
axes[0,1].set_title('square-root')
sns.histplot(ax=axes[0,2], data=wide_data, x="midterm", bins=bin_rice(wide_data["midterm"]))
axes[0,2].set_title('rice')
sns.histplot(ax=axes[1,0], data=wide_data, x="midterm", bins=bin_sturge(wide_data["midterm"]))
axes[1,0].set_title('sturge')
sns.histplot(ax=axes[1,1], data=wide_data, x="midterm", bins=bin_scott(wide_data["midterm"]))
axes[1,1].set_title('scott')
sns.histplot(ax=axes[1,2], data=wide_data, x="midterm", bins=bin_fd(wide_data["midterm"]))
axes[1,2].set_title('freedman-diaconis')
#plt.show() # uncomment to show
plt.close()

##########
# Task 5 #
##########
"""
5A: Is it meaningful to have a bin-count of 1?
No

5B: Is it meaningful to have a bin-count roughly equal
    to length of values N?
No

"""

##########
# Task 6 #
##########

def order_by_median(wide_data, cat, num):
    cat_list = wide_data[cat] #list of this category
    num_list = wide_data[num] #list of this numerical
    
    
        

"""
6B: Does the data suggest an incoming MED student
    is more likely to perform better than an incoming
    student from another faculty? Explain.
Yes. Median of MED is higher than the median of the rest of the faculties.
"""

cat_col = "faculty"
num_col = "total"
cat_order = order_by_median(wide_data, cat_col, num_col)

# Task 6 Testcases
print(cat_order) # ['MED', 'NUSHS', 'LAW', 'SOC', 'FOE', 'FOS', 'BIZ', 'FASS', 'SDE']

sns.boxplot(x=cat_col, y=num_col, data=wide_data, order=cat_order)
plt.title("Distribution of total by faculty")
#plt.show() # uncomment to show
plt.close()

##########
# Task 7 #
##########

# Provided code to produce scatter plot of level and total

#sns.scatterplot(x='level', y='total', data=wide_data, hue='faculty', style='faculty', s=15)
#plt.title("Students' total against Students' level")
#plt.show() # uncomment to show
#plt.close()


# 7A: Your code to complete, to replace the ...
sns.scatterplot(x=..., y=..., data=..., hue='faculty', style='faculty', s=15)
plt.title("Students' final against Students' midterm")
#plt.show() # uncomment to show
plt.close()

"""
7B: State the trend in the scatter plot produced in 7A
The trend is generally linear but with a wide spread. Most students who perform better for midterm also perform better for finals. However, there are cases where low midterm still resulted in better finals and vice versa.

7C: Is your friend's claim justified? Explain.
No. This is just a general trend, there are cases of low midterm people scoring well for finals, perhaps it just means a minor setback in the beginning but it is still possible to catchup. This friend could be like the blue point that is rather segregated at final=80 and midterm = 12
"""
