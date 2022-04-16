import sys

argvs = sys.argv

with open(argvs[1],'r') as f:
    lines =  f.read().split('\n')
    for line in lines:
        print(line)
        for c in line:
            print(c)

