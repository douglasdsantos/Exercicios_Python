'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso.
Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. 
Caso contrário mostrar tais variáveis com o conteúdo ZERO.'''

peso_peixes = float(input('Digite a quantidade de Kilos de peixe: '))
if peso_peixes <= 50:
    multa = 0
    print('Você não pagará multa. \nValor da multa {:.2f}' .format(multa))
else:
    peso_excedente = peso_peixes - 50
    multa = peso_excedente * 4
    print('Valor da multa a pagar R${:.2f} \nPois excedeu em {:.2f}kg(s)' .format(multa, peso_excedente))
