"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.

 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
   
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
   
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
------------------------------------------------------
Part B:

    What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits.

"""


# Part A
def find_area(calls):
    
    # Getting the codes
    lst = []
    for call in calls:
        if '(0' in call[1]:
            lst.append(brackets(call))
        elif ' ' in call[1] and call[1][0] in ['7','8','9']:
             lst.append(call[1][:4])
        elif call[1][:3] == '140':
            lst.append('140')
    
    return lst
    
def sorted_unique(lst):
    return sorted(list(set(lst)))

def brackets(call):
    
    '''This is a helper function'''
    return call[1].split(sep=')')[0] + ')'


print("The numbers called by people in Bangalore have codes:")

# Listing all the area codes
lst_all = find_area(calls)
# storing the length
length = len(lst_all)
# Listing the unique area codes
lst = sorted_unique(lst_all)


# Printing all the values.
for code in lst:
    print(code)

# --------------------------------------------------------------- #

# Part B

def count_080(calls):
    count = 0
    for call in calls:
        if '(080)' == call[1][:5]:
            count+=1
    return count
            
    

count = count_080(calls)
print()
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(count/length*100))
