def count(p, c):
    total = 0
    for letra in p:
        if letra == c:
            total = total + 1
    return total

palavra = input("Informe uma palavra: ")
caracter = input("Informe uma letra para ser contada: ")

total = count(palavra,caracter)
print("Existe(m) "  + str(total) +  " ocorrência(s) de '" + caracter + "' em "  + palavra)