import sys

for line in sys.stdin:
    data = line.strip().split(',')

    if len(data)!=9:
        continue

    # if data[3]=='2013':
    path = data[3].split(" направление ")
    if len(path)<2:
        continue

    path = path[1].split(")")[0]
    data[3] = path
    # print(data[3].split(" направление ")[1])
    if data[2]=='2013':
        print(f"{data[3]},{data[4]}")