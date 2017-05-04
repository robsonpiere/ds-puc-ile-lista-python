total = 0
fhand = open("mbox.txt")
for line in fhand:
    palavras = line.split()
    if (len(palavras) > 1) and (palavras[0] == "From"):
        print (palavras[1])
        total += 1
print("%d linhas no arquivo possuem From como primeira palavra" %total)