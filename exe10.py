#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
# F = °C * 1,8 + 32

celsius = float(input('Digite a temperatura em Celsius: '))
farenheit = (celsius * 1.8) + 32
print('A temperatura de {} °C equivale a {} °F.' .format(celsius, farenheit))
