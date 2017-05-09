print("Informe um valor entre 0.0 e 1.0")

try:
    numero = float(input())
    if numero > 1.0 or numero < 0.0:
        print("Pontuação fora do intervalo!")
    elif numero >= 0.9:
        print("Pontuação: A")
    elif numero >= 0.8:
        print("Pontuação: B")
    elif numero >= 0.7:
        print("Pontuação: C")
    elif numero >= 0.6:
        print("Pontuação: D")
    else:
        print("Pontuação: F")
except:
    print("Meu jovem, é pra digitar um número")
finally:
     print("Programa finalizado")