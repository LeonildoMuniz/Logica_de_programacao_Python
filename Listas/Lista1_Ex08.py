'''
Faça um Programa que pergunte quanto você ganha por hora e 
o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
'''

a=float(input("Qual valor você ganha por hora:"))
b=float(input("Quantas horas foram trabalhadas:"))

salario=a*b

print(f'Salario a receber {salario: .2f}')
