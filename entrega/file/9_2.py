dias = dict()
arquivo = input("Digite o nome do arquivo: ")

try:
    fhand = open(arquivo)
    for line in fhand:
        palavras = line.split()
        if len(palavras) <= 2 : continue
        if palavras[0] != "From" : continue
        dia = palavras[2]
        if dia in dias:
            dias[dia] += 1
        else:
            dias[dia] = 1
    print(dias)
except FileNotFoundError:
    print("Não foi possível abrir o arquivo")
finally:
    print("Fim")