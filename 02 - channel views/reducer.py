import sys

number_of_items = int(sys.stdin.readline().strip())
shows = {}
for i in range(0, number_of_items):
    shows[sys.stdin.readline().strip()] = int(0)

for line in sys.stdin:
    data = line.strip().split(',')
    if(len(data)!=2):
        continue

    show, nums = data
    if show in shows:
        shows[show]+=int(nums)

for key in shows:
    print(f"{key} {shows[key]}")
