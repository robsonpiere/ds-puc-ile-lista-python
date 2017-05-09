print("Informe o número de horas trabalhadas: ", end=" ")
horas_trabalhadas = float(input())
print("Informe o valor pago por hora:", end=' ')
valor_hora = float(input())

salariobruto = horas_trabalhadas * valor_hora
print("O valor do salário bruto é: " + str(salariobruto))
