'''
This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER) When you have run the program on mbox.txt upload the resulting database file above for grading.

If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments:http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATEstatement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.

'''

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#starts with a fresh database each time this code runs
cur.execute('DROP TABLE IF EXISTS Counts')

#creating rows/columns in database
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER) ''')

#opening mbox.txt
fname = 'mbox.txt'
fh = open(fname)

#start reading through the file grabbing email domains and counting them (dictionary style)
for line in fh:
    if not line.startswith('From: '):continue
    line = line.split()
    emails = line[1]
    domains = emails.split('@')
    domains_storage = domains[1]
    #print(domains_storage)


###no idea what this does###
    cur.execute('SELECT count FROM Counts WHERE org = ?', (domains_storage,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (domains_storage,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domains_storage,))
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
###no idea what this does###
