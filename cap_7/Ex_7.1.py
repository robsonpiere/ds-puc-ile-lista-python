fhand = open("mbox-short.txt")

for line in fhand:
    linha = str(line).strip()
    print(linha.upper())
print("Arquivo lido com sucesso")