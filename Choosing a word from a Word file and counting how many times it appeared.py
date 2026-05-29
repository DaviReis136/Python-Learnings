fname = input('Digite o nome do arquivo: ')
fhand = open(fname)

count = dict()

for line in fhand:
    if not line.startswith('From '):
        continue

    palavras = line.split()
    email = palavras[1]

    count[email] = count.get(email, 0) + 1

bigcount = None
bigword = None

for email, value in count.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        bigword = email

print (bigword, bigcount)    
