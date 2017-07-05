#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

farenheit = float(input('Digite a temmperatura em Farenheit: '))
celsius = (5 * (farenheit - 32) / 9)
print('A temperatura de {} °F equivale a {:.2f} Graus °C.' .format(farenheit, celsius))