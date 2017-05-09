import os

for nome in os.listdir('./file'):
    dados = str(nome).split(".")
    numero = dados[0].split("_")[1]
    subnumero = dados[1]
    novo_nome = numero + "_" + subnumero + ".py"
    os.rename("./file/"+nome, "./file/"+novo_nome)
    print("arquivo " + nome + " alterado para " + novo_nome)