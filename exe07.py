# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
lado_quadrado = float(input('Digite o lado do quadrado: '))
area = lado_quadrado * lado_quadrado
print('A área do quadrado com lados de {} é igual a {:.2f}' .format(lado_quadrado, area))