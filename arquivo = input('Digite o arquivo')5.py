arquivo = input('Digite o arquivo')
if len(arquivo) < 1: 
    arquivo = 'mbox-short.txt'
    arquivo_aberto = open(arquivo)
if len(arquivo) >= 1:
    arquivo_aberto = open(arquivo)

arquivo_aberto = arquivo_aberto    
dicionario = dict () 

for line in arquivo_aberto:
    line = line.rstrip
    palvaras = line.split 

for linha in palvaras:
    dicionario[linha] = dicionario.get (linha,0) + 1

maior_palavra = None
Maior_count = None

for tupla1, tupla2 in dicionario.items(): 
    for linha1 in dicionario.items: 
        if tupla1 is None or tupla1 > Maior_count:
            Maior_count = tupla1 
            maior_palavra = tupla2 

print(maior_palavra, Maior_count)
