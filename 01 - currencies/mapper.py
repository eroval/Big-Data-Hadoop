#!/usr/bin/python
import sys

file = sys.stdin


# get name of fields as key with corresponding value 
# as list
keys = []
for key in file.readline().strip().split(","):
    keys.append(key)

next(file)

for line in file:
    data = line.strip().split(",")
    
    try:
        continue_print=True
        for value in data:
            if not value:
                continue_print=False
        if continue_print:
            
            print(data[1],data[0], data[2])
    except:
        print("could not get data")
        # do nothing, do not print
        pass