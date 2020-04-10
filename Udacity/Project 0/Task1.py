"""
The text and call data are provided in csv files.

The text data (text.csv) has the following columns: sending telephone number (string), 
receiving telephone number (string), timestamp of text message (string).

The call data (call.csv) has the following columns: calling telephone number (string),
 receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def get_telephone(lsts1,lsts2):
    
    # Creating an empty list for outcoming calls
    calls = []
    
    for lst1,lst2 in zip(lsts1,lsts2):
        
        # Appending the calls from list 1.
        calls.append(lst1[0])
        calls.append(lst1[1])
        
        # Appending the calls from list 2.
        calls.append(lst2[0])
        calls.append(lst2[1])       
        
    return len(list(set(calls)))

# Printing the elements.
print("There are {} different telephone numbers in the records.".format(get_telephone(texts,calls)))