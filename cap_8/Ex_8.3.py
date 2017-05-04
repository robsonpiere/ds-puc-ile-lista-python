fhand = open("mbox-short-erro.txt")
count = 0
for line in fhand:
    palavras = line.split()
    #print ("Debug:", palavras)
    if (len(palavras) > 2) and (palavras[0] == "From"):
        print (palavras[2])