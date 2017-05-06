try:
    arquivo = input("Informe o nome do arquivo: ")
    fhand = open(arquivo)
    for line in fhand:
        linha = str(line).strip()
        print(linha.upper())
    print("Arquivo lido com sucesso")
except FileNotFoundError:
    print("o arquivo não foi localizado, verifique o caminho informado")


