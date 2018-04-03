import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#starts with a fresh database each time this code runs
cur.execute('DROP TABLE IF EXISTS Counts')

#creating rows/columns in database
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER) ''')

#opening mbox.txt
fname = 'mbox.txt'
fh = open(fname)

#start reading through the file grabbing emails and counting them (dictionary style)
for line in fh:
    if not line.startswith('From :'):continue
    pieces = line.split()
    emails = pieces[1]
       
