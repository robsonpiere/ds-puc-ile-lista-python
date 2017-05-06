import re
import unicodedata

def removerCarateres(texto):
    texto = str(texto).lower()
    texto = unicodedata.normalize('NFKD',texto)
    return re.sub('[^a-z]','',texto)

def unirTexto(arquivo):
    texto = str()
    for linha in arquivo:
        nova = removerCarateres(linha)
        texto += nova
    return texto

def contaCaracteres(arquivo):
    letras = dict()
    ordenado = list()
    textoLimpo = unirTexto(arquivo)
    for letra in textoLimpo:
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1
    for letra in letras:
        ordenado.append((letra,letras[letra]))
    ordenado.sort(key= lambda x: x[1],reverse=True)
    return ordenado

try:
    caminho = input("Informe o aquivo a ser contado: ")
    arquivo = open(caminho)
    lista = contaCaracteres(arquivo)
    print("Ordem de aparição das letras")
    for item in lista:
        print(item)
except FileNotFoundError:
    print("Não foi possível abrir o arquivo, verifique o caminho informado.")
