import sys

file = open(sys.argv[1])

for line in file:
    line = line.rstrip()
    index = 0
    for i, v in enumerate(line):
        if(index % 2 == 0):
            v = v.upper()
        else:
            v = v.lower()
        if v.isalpha():
            index+=1
        print(v, end="")
    print()