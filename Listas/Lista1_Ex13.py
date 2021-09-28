'''
Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

'''

a=float(input("Digite sua altura:"))
b=input("Digite seu sexo M/F:")

if b=='M':
	imc=(72.7*a)-58
else:
	imc=(62.1*a)-44.7


print(f'Seu peso ideal é: {imc: .2f}')
