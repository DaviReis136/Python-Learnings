#arquvo de e-mail da empresa
arquivo = open('mbox-short.txt')

for linha in arquivo: 
    #removendo newlines
    lina = linha.rstrip()
    print('linha', linha)
    #dividindo cada linha em lista / palavras
    palavras = linha.split()
    print ('palavras',palavras)
    #Caso a primera palavra (0) não for De ignora 
    if palavras[0] != 'De' :
        print('Ignore')
        continue
    #Caso for printa a segunda palavra da frase
    print(palavras[2])
 
#Acima deu errado, mas vamos printar cada etapa, afim de identificar o erro.
#Descobrindo que precisamos dua Guardian, linha que protege o erro das demais.
#No caso o erro é em relação as linhas vazias

for linha in arquivo: 
    #removendo newlines
    lina = linha.rstrip()
    print('linha', linha)
    #dividindo cada linha em lista / palavras
    palavras = linha.split()
    print ('palavras',palavras) 
    #linha Guardian caso palavra for menor do que 1 não abre evitando os espaços em branco
    if len(palavras) < 1: 
        continue
    #ou podemos escrever
    if palavras == '': 
        print('linha em branco')
        continue  
    #Caso a primera palavra (0) não for De ignora 
    if palavras[0] != 'De' :
        print('Ignore')
        continue
    #Caso for printa a segunda palavra da frase
    print(palavras[2])

#A guardian forte pra esse caso seria especificamente
#len(palavras) < 2, pois evitamos o proseguimento de qualquer linha que 
#começe por palavra menor que 4 letras 'De'. 
 
for linha in arquivo: 
    #removendo newlines
    lina = linha.rstrip()
    #dividindo cada linha em lista / palavras
    palavras = linha.split()
    #Linha Guardian deve ter preferência / lida primeiro
    #Caso a primera palavra (0) não for De ignora 
    if len(palavras) < 2 or palavras[0] != 'De': 
        continue
    #Caso for printa a segunda palavra da frase
    print(palavras[2])
