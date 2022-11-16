#!/usr/bin/python
import sys

times_met = 0
mapped_key = None

for line in sys.stdin:
    data = line.strip()

    if mapped_key and mapped_key != data:
        # it's a new one - reset
        print(mapped_key, "\t", times_met)
        mapped_key = data
        times_met = 0

    mapped_key = data
    times_met += 1

if mapped_key != None:
    print (mapped_key, "\t", times_met)
