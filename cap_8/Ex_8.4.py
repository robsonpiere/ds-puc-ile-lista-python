lista = []
fhand = open("romeo.txt")
for line in fhand:
    palavras = line.split()
    for palavra in palavras:
        if palavra in lista : continue
        lista.append(palavra)
lista.sort()
print(lista)