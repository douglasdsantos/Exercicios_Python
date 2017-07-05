'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 
8% para o INSS e 
5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
vlr_hora = float(input('Digite o valor de sua hora trabalhada: R$  '))
qtd_horas = float(input('Digite a quantidade de horas trabalhadas no mês: '))
print()
salario_bruto = vlr_hora * qtd_horas
ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sindicato = (salario_bruto * 5) / 100
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print('+ Salário Bruto : \t R$ {:.2f}' .format(salario_bruto))
print('- IR (11%) : \t\t R$ {:.2f}' .format(ir))
print('- INSS (8%) : \t\t R$ {:.2f}' .format(inss))
print('- Sindicato (5%) : \t R$ {:.2f}' .format(sindicato))
print('= Salário Líquido : \t R$ {:.2f}' .format(salario_liquido))