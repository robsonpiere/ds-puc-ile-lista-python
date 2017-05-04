numeros = []

while True:
    try:
        entrada = input("Digite ou numero ou 'pronto' para sair: ")
        if entrada.lower() == "pronto":
            break
        numero = float(entrada)
        numeros.append(numero)
    except:
        print("Digite um número meu jovem...")

print("Foram digitados %d números" %len(numeros))
if len(numeros) > 0:
    print("Valor máximo: %d" %max(numeros))
    print("Valor mínimo: %d" %min(numeros))