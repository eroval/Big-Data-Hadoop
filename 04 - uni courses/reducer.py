import sys

sum_value = 0
old_course = None

for line in sys.stdin:
    course, value = line.strip().split(",")
    value = int(value)

    if old_course and old_course!=course:
        print(f"{old_course}: {sum_value}")
        sum_value = value

    old_course = course
    sum_value = sum_value + value

if old_course:
    print(f"{old_course}: {sum_value}")