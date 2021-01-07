"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

def finding_Duration(my_List):
    Num_dict=dict()
    Number = None 
    getDuration = 0
    for calling, receiving, date_Time, Duration in my_List:
        Num_dict[calling] = Num_dict.get(calling,0) + int(Duration)
        if Num_dict[calling] > getDuration:
            Number = calling
            getDuration = Num_dict[calling]
        Num_dict[receiving] = Num_dict.get(receiving,0) + int(Duration)
        if Num_dict[receiving] > getDuration:
            Number = receiving
            getDuration = Num_dict[receiving]
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(Number, getDuration))

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    finding_Duration(calls)
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
