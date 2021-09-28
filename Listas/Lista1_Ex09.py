'''
Faça um Programa que peça a temperatura em graus Farenheit, 
transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).

'''

a=float(input("Digite a temperatura em graus Farenheit:"))

c=(5*(a-32)/9)


print(f'Temperatura em graus Celsius {c: .2f}')
