numeros = []

while True:
    try:
        entrada = input("Digite ou numero ou 'done' para sair:")
        if entrada == "done":
            break
        numero = float(entrada)
        numeros.append(numero)
    except:
        print("Bad Data")

if len(numeros) > 0:
    print("Valor máximo:" + str(max(numeros)))
    print("Valor mínimo:" + str(min(numeros)))
else:
    print("Nenhum número informado.")