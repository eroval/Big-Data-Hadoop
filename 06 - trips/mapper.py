#!/usr/bin/python
import sys

my_map = {}

fields = sys.stdin.readline().strip().split(",")
it = 0
for key in fields:
    my_map[key] = it
    it+=1


for line in sys.stdin:
    data = line.strip().split(",")
    print(data[my_map["vendor_id"]]+","+data[my_map["trip_duration"]])
