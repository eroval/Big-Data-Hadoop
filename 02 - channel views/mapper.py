import sys

file = sys.stdin
shows = set()

for line in file:
    data = line.strip().split(",")
    if len(data)!=2:
        continue
    show, tv = data

    if tv == 'ABC':
        shows.add(show)

print(len(shows))
for value in shows:
    print(value)