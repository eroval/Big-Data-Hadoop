#!/usr/bin/python
import sys
for line in sys.stdin:
    data = line.strip().split(" ")
    
    if "php" in data[7]:
        print(data[7])
