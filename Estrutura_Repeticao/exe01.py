# Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um outro valor: '))

if num1 > num2:
    print('O maior número é {}' .format(num1))
elif num2 > num1:
    print('O maior número é {}' .format(num2))
else:
    print('Números iguais...')
