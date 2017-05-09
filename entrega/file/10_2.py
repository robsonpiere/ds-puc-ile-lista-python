horas = dict()
arquivo = input("Digite o nome do arquivo: ")
lista = list()
try:
    fhand = open(arquivo)
    for line in fhand:
        palavras = line.split()
        if len(palavras) <= 5 : continue
        if palavras[0] != "From" : continue
        hora = palavras[5].split(":")[0]
        if hora in horas:
            horas[hora] += 1
        else:
            horas[hora] = 1
    for hora in horas:
        lista.append((hora,horas[hora]))
    lista.sort(key= lambda x: x[0])
    for hora in lista:
        print(hora)      
except FileNotFoundError:
    print("Não foi possível abrir o arquivo")
finally:
    print("Fim")