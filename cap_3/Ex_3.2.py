
try:
    print("Informe o número de horas trabalhadas: ", end=" ")
    horas_trabalhadas = float(input())
    print("Informe o valor pago por hora:", end=' ')
    valor_hora = float(input())

    if horas_trabalhadas > 40:
        salariobruto = horas_trabalhadas * (valor_hora * 1.5)
    else:
        salariobruto = horas_trabalhadas * valor_hora
    print("O valor do salário bruto é: " + str(salariobruto))
except:
    print("Erro! Por favor, digite uma entrada numérica.")
finally:
    print("Execução do programa finalizada...")


