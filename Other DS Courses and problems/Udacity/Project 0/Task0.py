"""
The text data (text.csv) has the following columns: sending telephone number (string), 
receiving telephone number (string), timestamp of text message (string).

The call data (call.csv) has the following columns: calling telephone number (string), 
receiving telephone number (string), start timestamp of telephone call (string), 
duration of telephone call in seconds (string)

"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# Function 1
# Speed Complexity analysis is O(1), No extra variables needed needed
def get_first(lst):
    '''Function: Gets the first record in a the list of lists and splits its elements 
    
        Input: List
        Output: Set
    
    '''
    return (lst[0][0],lst[0][1],lst[0][2])

# Function 2
# Speed Complexity analysis is O(1), No extra variables needed needed
def get_last(lst):
    return (lst[-1][0],lst[-1][1],lst[-1][2])
    
 # Texts : Speed Complexity analysis is O(1)  
incoming, answering, time = get_first(texts)
print("First record of texts, ",incoming," texts ",answering," at time ",time)

# Calls: Complexity analysis is O(1)  
incoming, answering, time = get_last(calls)
print("First record of calls, ",incoming," calls ",answering," at time ",time)













