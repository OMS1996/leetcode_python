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
TASK 4:
    
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

## What they do
# Extracting the out_going calls: They send out
out_going = set([call[0] for call in calls])

## What they don't do
# Extracting the incoming calls: They DONT recieve.
incoming = set([call[1] for call in calls])
# Extracting the texts: They don't Send text.
rec = set([text[0] for text in texts])
# Extracting the texts: They don't Send text.
send = set([text[1] for text in texts])

# Excluding the sets and keeping what remains.
out_going = out_going.difference(incoming)
out_going = out_going.difference(rec) 
out_going = out_going.difference(send)

# Sorting it.
out_going = sorted(out_going)

# The Print statement.
print("These numbers could be telemarketers: ")
# Printing One By One for Clarity.
for out in out_going:
    print(out)


