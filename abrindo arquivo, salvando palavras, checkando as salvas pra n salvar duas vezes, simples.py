#abrir o arquivo 
fname = input("Enter file name: ")
fh = open(fname)

#ele quer que angt abra ele leia cada palvra e salve, e verifica se já foi salvo pra não ter 2 saves.

#Onda angt salva cada palavra
words = []

#Remover newlines e dividir em lista do arquivo

for line in fh:
    line = line.rstrip()
    wds = line.split()
    
    # verificar se já foi salva, as palavras do arquivo editado acima. Se não angt salva.

    for w in wds:
        if w not in words:
            words.append(w)

#vamos mudar a ordem das palavras salvas não-repetidas e printar.

words.sort()
print(words)