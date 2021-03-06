'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.

You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
storage = dict()
fh = open("mbox-short.txt","r")
for line in fh:

    line = line.rstrip()
    if line.startswith("From "):
        line = line.split()
        hour = line[5].split(":")[0]
        if hour not in storage.keys():
            storage[hour] = 1
        else:
            storage[hour] += 1

for k,v in sorted(storage.items()):
    print(k,v)



'''
Desired output:
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''
