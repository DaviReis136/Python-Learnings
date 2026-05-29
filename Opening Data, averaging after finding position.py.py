line3 = 0.0
count = 0

try:
    fname = input("Enter file name: ")
    fh = open(fname)
except: 
    print('wrong')
    quit()

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    Pos = line.find(":")
    line1 = line[Pos+1:]    
    count = count + 1
    line2 = float(line1)
    line3 = line3 + line2 
    line4 =  line3 / count

print("Average spam confidence:", line4)
