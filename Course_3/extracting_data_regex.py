import re
numlist = []
output = []
fh = open("regex_sum_72204.txt","r")
for line in fh:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if x == []:continue
    for i in x:
        numlist.append(i)

for number in numlist:
    number = int(number)
    output.append(number)

print(sum(output))
