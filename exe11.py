# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input('Digite um valor Inteiro (Sem virgula):  '))
n2 = int(input('Digite outro valor Inteiro (Sem virgula):  '))
n3 = float(input('Digite um valor Real (Com virgula):  '))

result1 = (n1 * 2) * (n2 / 2)
result2 = (n1 * 3) + n3
result3 = n3 ** 3

print(result1)
print(result2)
print(result3)