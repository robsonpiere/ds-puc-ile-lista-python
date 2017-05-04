#Caso de teste = adicionada uma linha contendo somente a palavra From, causando erro de indice

#fhand = open("mbox-short-erro.txt")
#count = 0
#for line in fhand:
#    palavras = line.split()
#    #print ("Debug:", palavras)
#    if len(palavras) == 0 : continue
#    if palavras[0] != "From" : continue
#    print (palavras[2])


fhand = open("mbox-short-erro.txt")
count = 0
for line in fhand:
    palavras = line.split()
    #print ("Debug:", palavras)
    if len(palavras) <= 1 : continue
    if palavras[0] != "From" : continue
    print (palavras[2])