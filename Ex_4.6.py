def computepagamento(horas_trabalhadas,valor_hora):
    if horas_trabalhadas > 40:
        salariobruto = horas_trabalhadas * (valor_hora * 1.5)
    else:
        salariobruto = horas_trabalhadas * valor_hora
    return salariobruto

try:
    horas_trabalhadas = float(input("Informe o número de horas trabalhadas:  "))
    print("Informe o valor pago por hora:", end=' ')
    valor_hora = float(input())    
    print("O valor do salário bruto é: " + str(computepagamento(horas_trabalhadas,valor_hora)))
except:
    print("Erro! Por favor, digite uma entrada numérica.")
finally:
    print("Execução do programa finalizada...")