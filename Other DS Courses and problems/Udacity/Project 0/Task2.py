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

def get_numbers(calls):
    nums = set()
    for call in calls:
        nums.update([call[0],call[1]])
    return nums
        


def longest_time(calls):
    '''
    function to get index and maximum value with BigO(n)
    '''
    # getting all the Unique phone numbers.
    nums = get_numbers(calls)
    
    # Creating a dictionary and intializing it with Zero for its values.
    call_dict = dict()
    # From Keys
    call_dict = dict.fromkeys(nums,0)
    
    # Getting all the call counts.
    for call in calls:
        call_dict[call[0]] += int(call[3])
        call_dict[call[1]] += int(call[3])
    return call_dict

# dictionary creation
call_dict = longest_time(calls)

# Getting the largest value key and time.
key = max(call_dict, key=call_dict.get)
time = call_dict[key]
    


# Printing the required answers.
print("{} spent the longest time, {} seconds, on the phone during \
September 2016.".format(key,time))









