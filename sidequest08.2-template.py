#
# CS1010S --- Programming Methodology
#
# Sidequest 08.2 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

possible_birthdays = (('May', '15'),
                      ('May', '16'),
                      ('May', '19'),
                      ('June', '17'),
                      ('June', '18'),
                      ('July', '14'),
                      ('July', '16'),
                      ('August', '14'),
                      ('August', '15'),
                      ('August', '17'))

# (May, June, July, August) (14,15,16,17,18,19)
# Albert and Bernard just became friends with Cheryl,
# and they want to know when her birthday is.
# Cheryl gave Albert and Bernard a tuple of 10 possible dates.

#############
# Task 1(a) #
#############

def unique_day(day, possible_birthdays):
    count = 0
    for bday in possible_birthdays:
        if day==bday[1]:
            count+=1
        else:
            continue
    if count==1:
        return True
    else:
        return False
            

print("\n## Task 1a ##")
print(unique_day("16", possible_birthdays)) # False
print(unique_day("17", possible_birthdays)) # False
print(unique_day("18", possible_birthdays)) # True
print(unique_day("19", possible_birthdays)) # True

#############
# Task 1(b) #
#############

def unique_month(month, possible_birthdays):
    count = 0
    for bday in possible_birthdays:
        if month==bday[0]:
            count+=1
        else:
            continue
    if count==1:
        return True
    else:
        return False

print("\n## Task 1b ##")
print(unique_month('May', possible_birthdays)) # False
print(unique_month('June', possible_birthdays)) # False
print(unique_month('March', (('August', '1'), ('March', '2'), ('March', '3')))) # False
print(unique_month('August', (('August', '1'), ('March', '2'), ('March', '3')))) # True

#############
# Task 1(c) #
#############

def contains_unique_day(month, possible_birthdays):
    bdays = tuple(filter(lambda x: x[0]==month, possible_birthdays))
    day_lst = []
    for bday in bdays:
        day_lst.append(bday[1])
    for day in day_lst:
        if day_lst.count(day)==1:
            if unique_day(day,possible_birthdays)==True:
                return True
            else:
                continue
        else:
            continue
    return False
                

print("\n## Task 1c ##")
print(contains_unique_day("May", possible_birthdays)) # True
print(contains_unique_day("June", possible_birthdays)) # True
print(contains_unique_day("July", possible_birthdays)) # False

#############
# Task 2(a) #
#############

# Albert (given month):
# I don't know Cheryl's birthday, but I know that Bernard doesn't know too.

def statement1(birthday, possible_birthdays):
    m = birthday[0]
    if unique_month(m,possible_birthdays)==False and contains_unique_day(m, possible_birthdays)==False:
        return True
    else:
        return False
        

print("\n## Task 2a ##")
print(statement1(('May', '19'), possible_birthdays)) # False
print(statement1(('August', '14'), possible_birthdays)) # True

#############
# Task 2(b) #
#############

# Bernard (given day):
# At first I didn't know when Cheryl's birthday is, but I know now.

def statement2(birthday, possible_birthdays):
    d = birthday[1]
    if unique_day(d,possible_birthdays)==True:
        return True
    else:
        return False

print("\n## Task 2b ##")
print(statement2(('May', '19'), possible_birthdays)) # True
print(statement2(('August', '14'), possible_birthdays)) # False
print(statement2(('August', '17'), possible_birthdays)) # False
print(statement2(('July', '16'), possible_birthdays)) # False

#############
# Task 2(c) #
#############

# Albert (given month):
# Then I also know when Cheryl's birthday is.

def statement3(birthday, possible_birthdays):
    m = birthday[0]
    if unique_month(m, possible_birthdays)==True:
        return True
    else:
        return False

print("\n## Task 2c ##")
print(statement3(('May', '19'), possible_birthdays)) # False
print(statement3(('August', '14'), (('August', '14'),))) # True

##########
# Task 3 #
##########

# Based on statement 1, we can filter out some birthdays.
# From statement 2, we can filter out some more birthdays.
# Finally, using statement 3, we can filter out the remaining wrong birthdays.

def get_birthday(possible_birthdays):
    bday = list(filter(lambda x: statement1(x, possible_birthdays),list(possible_birthdays)))
    bday = list(filter(lambda x:statement2(x, bday),bday))
    bday = tuple(filter(lambda x: statement3(x, bday), bday))
    return bday

print("\n## Task 3 ##")
print(get_birthday(possible_birthdays)) # (('July', '16'),)
