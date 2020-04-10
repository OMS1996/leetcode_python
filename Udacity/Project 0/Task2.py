"""
Read file into texts and calls.
It's ok if you don't understand how to read files

The call data (call.csv) has the following columns:

 calling telephone number (string),
 
 receiving telephone number (string), 
 
 start timestamp of telephone call (string),
 
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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.

Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".

"""



def highest(calls):
    '''
    function to get index and maximum value with BigO(n)
    '''
    longest_call = -99
    i = -1
    for lst in calls:
        # getting the next index.
        i+=1
        # The amount of time.
        call_duration = int(lst[3])
        
        if longest_call  < call_duration:
            longest_call  = call_duration
            index = i
    return index,longest_call 

# Getting the values.
index,longest = highest(calls)

# Printing the required answers.
print("{} spent the longest time, {} seconds, on the phone during \
September 2016.".format(calls[index][0],longest))









