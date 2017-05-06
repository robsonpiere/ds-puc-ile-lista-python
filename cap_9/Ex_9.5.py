dominios = dict()
arquivo = input("Digite o nome do arquivo: ")
try:
    fhand = open(arquivo)
    for line in fhand:
        palavras = line.split()
        if len(palavras) <= 2 : continue
        if palavras[0] != "From" : continue
        email = palavras[1]
        posicao = email.find("@")
        dominio = email[posicao +1:]
        if dominio in dominios:
            dominios[dominio] += 1
        else:
            dominios[dominio] = 1
    print("Lista de domínios:")
    print(dominios)
except:
    print("Não foi possível abrir o arquivo")
finally:
    print("Fim")