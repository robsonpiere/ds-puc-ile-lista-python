emails = dict()
arquivo = input("Digite o nome do arquivo: ")

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
        m_email = ""
        total = 0
        for email in emails:
            if emails[email] > total:
                m_email = email
                total = emails[email]
    print("Email com mair número de envios:",end=" ")
    print(m_email,end=" : ")
    print(total)
except FileNotFoundError:
    print("Não foi possível abrir o arquivo")
finally:
    print("Fim")