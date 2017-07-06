# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input('Digite (M)Masculino ou (F)Feminino:  ')

if sexo == "M" or sexo == 'm':
    print('M - Masculino')
elif sexo == "F" or sexo == "f":
    print('F - Feminino')
else:
    print('Sexo inválido')