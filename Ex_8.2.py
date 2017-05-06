try:
    fhand = open("mbox-short-erro.txt")
    for line in fhand:
        palavras = line.split()
        #print ("Debug:", palavras)
        if len(palavras) <= 2 : continue
        if palavras[0] != "From" : continue
        print (palavras[2])
except FileNotFoundError:
    print("Ocorreu um erro ao abrir o arquivo")

#Caso de teste = adicionada uma linha contendo somente a palavra From, causando erro de indice