fname = input("Enter file name: ")
arquivo = open(fname)
count = 0

for line in arquivo:
    line = line.rstrip()
    line2 = line.split()
    if len(line2) < 3 or line2[0] != 'From': 
        continue
    print(line2[1])
    count = count + 1


print("There were", count, "lines in the file with From as the first word")
