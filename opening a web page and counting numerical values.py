import urllib.request
import re

url = "http://py4e-data.dr-chuck.net/regex_sum_2376851.txt"

arquivo = urllib.request.urlopen(url).read().decode()

numeros = re.findall('[0-9]+', arquivo)

soma = 0

for n in numeros:
    soma += int(n)

print(soma)
