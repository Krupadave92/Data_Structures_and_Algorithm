"""
Read file into texts and calls.
It's ok if you don't understand how to read files."""
"""TASK 1:
How many different telephone numbers are there in the records? 
Print a message:"""
"There are <count> different telephone numbers in the records."
"""
"""
import csv

Numbers_Calling = []
Numbers_Receiving_Calls = []
Numbers_Sending=[]
Numbers_Receiving_Texts=[]

def count_Unique_Number(my_ListCalls,My_ListTexts):
    for i in range(len(my_ListCalls)):
        Numbers_Calling.append(my_ListCalls[i][0])
        Numbers_Receiving_Calls.append(my_ListCalls[i][1])
    for i in range(len(My_ListTexts)):
        Numbers_Sending.append(My_ListTexts[i][0])
        Numbers_Receiving_Texts.append(My_ListTexts[i][1])
    unique_Numbers=(set(Numbers_Calling + Numbers_Receiving_Calls + Numbers_Sending + Numbers_Receiving_Texts))
    return unique_Numbers
    
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

print ("There are ",len(count_Unique_Number(calls,texts)), " different telephone numbers in the records.")
