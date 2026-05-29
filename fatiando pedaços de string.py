text = "X-DSPAM-Confidence:    0.8475"
Pos = text.find(":")
POS1 = text[Pos+1:]
Valor = float(POS1)
print(Valor)

