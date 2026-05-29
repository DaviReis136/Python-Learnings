fname = input("Enter file name: ")
fh = open(fname)

counts = dict()

for line in fh:
    if not line.startswith("From "):
        continue
    
    words = line.split()
    email = words[1]
    
    counts[email] = counts.get(email, 0) + 1

bigcount = None
bigemail = None

for email, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = email

print(bigemail, bigcount)