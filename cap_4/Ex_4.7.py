def computegrau(pontuacao):
    if pontuacao > 1.0 or pontuacao < 0.0:
       return "Pontuação fora do intervalo!"
    elif pontuacao >= 0.9:
        return "A"
    elif pontuacao >= 0.8:
        return "B"
    elif pontuacao >= 0.7:
        return "C"
    elif pontuacao >= 0.6:
        return "D"
    else:
        return "F"
try:
    numero = float(input("Informe um valor entre 0.0 e 1.0: "))
    print(computegrau(numero))
except:
    print("Meu jovem, é pra digitar um número")
finally:
     print("Programa finalizado")