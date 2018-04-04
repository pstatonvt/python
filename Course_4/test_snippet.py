#opening mbox.txt
fname = 'mbox.txt'
fh = open(fname)

#start reading through the file grabbing emails and counting them (dictionary style)
for line in fh:
    if not line.startswith('From: '):continue
    line = line.split()
    emails = line[1]
    #print(emails)
    domains = emails.split('@')
    domains_storage = domains[1]
    print(domains_storage)
