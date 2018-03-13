import re

fh = open("regex_sum_72204.txt","r")
output = []
for line in fh:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if x == [] : continue
    for i in x:
        i = int(i)
        output.append(i)

print("Output:", sum(output))
