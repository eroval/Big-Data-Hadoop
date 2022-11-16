#!/usr/bin/python
import sys

file = sys.stdin


next(file)

for line in file:
    data = line.strip().split(",")
    
    try:
        continue_print=True
        for value in data:
            if not value:
                continue_print=False
        if continue_print:
            
            print(f"{data[1]},{data[0]},{data[2]}")
    except:
        print("could not get data")
        # do nothing, do not print
        pass