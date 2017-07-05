# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7 (h = altura)
# Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso

sexo = str(input('Digite seu sexo. (M)Masculino e (F)Feminino. '))

if sexo == 'M' or sexo == 'm':
    altura = float(input('Digite sua Altura: '))
    peso_ideal = (72.7 * altura) - 58
    print('Seu peso ideal é de {:.2f}.' .format(peso_ideal))

elif sexo == 'F' or sexo == 'f':
    altura = float(input('Digite sua Altura: '))
    peso_ideal = (62.1 * altura) - 44.7
    print('Seu peso ideal é de {:.2f}.' .format(peso_ideal))

else:
    print('Opção Inválida')