'''
Faça um Programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no 
referido mês, sabendo-se que são descontados 11% 
para o Imposto de Renda, 8% para o INSS e 5% para o 
sindicato, faça um programa que nos dê:
a -salário bruto.
b -quanto pagou ao INSS.
c -quanto pagou ao sindicato.
d -o salário líquido.
Calcule os descontos e o salário líquido, conforme a 
tabela abaixo:
f -+ Salário Bruto : R$
g - - IR (11%) : R$
h- - INSS (8%) : R$
i- - Sindicato ( 5%) : R$
j- = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.

'''

a=float(input("Digite quanto ganha por hora:"))
b=float(input('Digite o total de horas trabalhadas: '))

salarioBruto = a*b
ir=0.11
inss=0.08
sidicato=0.05
descontoTotal=ir+inss+sidicato

print(f'Salario Bruto: {salarioBruto: .2f}')
print(f'INSS pago: {salarioBruto*inss: .2f}')
print(f'Sindicato pago: {salarioBruto*sidicato: .2f}')
print(f'Salario Liquido: {salarioBruto-(salarioBruto*descontoTotal): .2f}')

