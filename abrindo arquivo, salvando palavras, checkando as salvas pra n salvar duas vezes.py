nome_arquivo = input()
arquivo = open(nome_arquivo)

palavras = []

for linha in arquivo:
    linha.rstrip()
    arquivo_arrumado = linha.split()

    for linha1 in arquivo_arrumado: 
        if linha1 not in palavras: 
            palavras.append(linha1)

palavras.sort()
print(palavras)


