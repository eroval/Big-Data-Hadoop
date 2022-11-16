#!/usr/bin/python
import sys
import math

old_price = None
old_name = None
my_map = {}

for line in sys.stdin:
    new_name, new_date, new_price = line.strip().split(",")
    new_price = float(new_price)
    

    if new_name not in my_map:
        my_map[new_name] = {}
        my_map[new_name]["%6.2f%%" % 0] = 1
    else:
        curr_percentage = ((new_price-old_price)/old_price)*100.00
        curr_percentage = round(curr_percentage, 2)
        curr_percentage = "%6.2f%%" % curr_percentage
        if curr_percentage not in my_map[new_name]:
            my_map[new_name][curr_percentage]=1
        else:
            my_map[new_name][curr_percentage]+=1

    old_price = new_price
    old_name = new_name

for key in my_map:
    for percentage in sorted(my_map[key]):
        print(f"{key}: {percentage}  {my_map[key][percentage]}")