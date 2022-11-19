#!/usr/bin/python
import sys

old_vendor_id = None
sum_trip_duration = 0

for line in sys.stdin:
    vendor_id, trip_duration = line.strip().split(",")
    trip_duration = int(trip_duration)

    if old_vendor_id and old_vendor_id != vendor_id:
        print(f"{old_vendor_id},{sum_trip_duration}")
        old_vendor_id = vendor_id
        sum_trip_duration = trip_duration

    old_vendor_id = vendor_id
    sum_trip_duration += trip_duration 

if old_vendor_id:
    print(f"{old_vendor_id},{sum_trip_duration}")
