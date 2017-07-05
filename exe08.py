# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

vlr_hora = float(input('Digite o valor que ganha por hora: '))
hora_mes = float(input('Digite a quantidade de horas trabalhadas no mês: '))
salario = vlr_hora * hora_mes

print('O seu salário mensal é de R$ {:.2f} reais.' .format(salario))