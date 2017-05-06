def limpar(palavra):
    caracteres = [",",".","-","?","!","%",":","\""]
    for caracter in caracteres:
        palavra = str(palavra).replace(caracter,"")
    return palavra
    
dicionario = dict()
arquivo = open("words.txt")

for linha in arquivo:
    palavras = linha.split()
    if len(palavras) == 0 :continue
    for palavra in palavras:
        palavra = limpar(palavra)
        if len(palavra)== 0:continue
        dicionario[palavra] = palavra

busca = input("Informe um termo para ser buscado no texto: ")
if busca in dicionario.values():
    print("Palavra " + dicionario[busca] + " localizada no texto.")
else:
    print("Palavra não localizada no texto.")
