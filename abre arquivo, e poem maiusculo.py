#abrindo o arquivo
try:
    fname = input("Enter file name: ")
    fh = open(fname)
except: 
    print('wrong')
    quit()

for fha in fh:
    fhu = fha.rstrip()
    #printando maiusculo
    print(fhu.upper()) 
    #Olha tem que que fica fhu.upper() porque upper e função
