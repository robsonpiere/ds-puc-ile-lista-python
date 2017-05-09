def chop(lista):
    tamanho = len(lista)
    if tamanho > 2 :
        del lista[tamanho-1]
        del lista[0]
    elif tamanho == 1:
        del lista[0]
    return None

lista = ["A","B","C","D","E","F"]
chop(lista)
print(lista)
