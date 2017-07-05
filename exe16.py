'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
''' 
metros = float(input('Digite a metragem a ser pintada: '))
# aqui divide a metragem por 3 pra saber quantos litros de tinta vai ser usado
litros = metros / 3
# definindo o valor da lata de tinta
preco_lata = 80.0
# definindo a quantidade de litros de uma lata de tinta
capacidade_litro = 18

# descobrindo a quantidade de latas de tinta
# dividindo litros pela capacidade de litros da lata
latas = litros /  capacidade_litro
# achando o valor que sera gasto para pintar
total = latas * preco_lata

print('Você usará {:.0f} latas de tinta.' .format(latas))
print('O valor total é de R${:.2f} ' .format(total))
