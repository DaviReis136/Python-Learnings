#Open Archive and look for From: 

a = input('Arquivo: ')
fl = open(a)

counts = dict() 

for line in fl: 
    if not line.startswith("From "):
        continue
    line = line.rstrip()
    words = line.split()
    
    time = words[5]
    hour = time.split(":")[0]

    counts[hour] = counts.get(hour, 0) + 1

for hour, count in sorted(counts.items()): 
    print(hour, count)
