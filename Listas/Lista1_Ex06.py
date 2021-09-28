'''
Faça um Programa que peça o raio de 
um círculo, calcule e mostre sua área.
'''

import math

a=float(input("Digite a medida do raio: "))

area=math.pi*(a**2) 

print(f'Valor da área do circulo: {area:.2f}')
