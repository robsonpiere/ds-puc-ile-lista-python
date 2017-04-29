soma = 0
quantidade = 0
media = 0

while True:
    try:
        entrada = input("Digite ou numero ou 'done' para sair:")
        if entrada == "done":
            break
        numero = float(entrada)
        quantidade += 1
        soma += numero
    except:
        print("Bad Data")

print("Total de números informados: " + str(quantidade))
print("Soma dos números informados: " + str(soma))
if quantidade == 0:
    print("Como não houve números digitados não foi possível calcular a média.")
else:
    print("Média do números informados: " + str(soma/quantidade))
    