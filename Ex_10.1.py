emails = dict()
arquivo = input("Digite o nome do arquivo: ")
lista = list()
try:
    fhand = open(arquivo)
    for line in fhand:
        palavras = line.split()
        if len(palavras) <= 2 : continue
        if palavras[0] != "From" : continue
        email = palavras[1]
        if email in emails:
            emails[email] += 1
        else:
            emails[email] = 1
    for email in emails:
        lista.append((email,emails[email]))
    lista.sort(key= lambda x : x[1],reverse=True)
    print("Email com mais envios:",end=' ')
    if len(lista) > 0 :
        print(lista[0])
    else:
        print("Não havia e-mails no texto")
except FileNotFoundError:
    print("Não foi possível abrir o arquivo")
finally:
    print("Fim")