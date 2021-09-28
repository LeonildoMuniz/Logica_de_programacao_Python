'''
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere 
que a cobertura da tinta é de 1 litro para 
cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de 
tinta a serem compradas e o preço total.

'''
import math

a=float(input("Informe o tamanho a ser pintado em m²: "))

total=math.ceil((a/3)/18)

print(f'Valor total a ser pago {total*80: .2f}')
