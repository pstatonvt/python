'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.

The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.

After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
fh = open("mbox-short.txt","r")
storage = dict()
lst = list()

for line in fh:
    line = line.rstrip()
    if line.startswith("From "):
        line = line.split()
        tmp = line[1]
        lst.append(tmp)

for name in lst:
    storage[name] = storage.get(name, 0) + 1


largest = None
for x in storage.values():
    if largest is None:
        largest = x
    if x > largest:
        largest = x

print(name,largest)
