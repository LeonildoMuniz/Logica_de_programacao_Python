al=1.9
ga=2.5

desA1=3
desA2=5
desG1=4
desG2=6

tipo=input('Digite o tipo de combustivel: A-álcool e G-gasolina: ')
litros=float(input('Digite o total de litros abastecidos: '))

print()
print('='*50)
print()

if litros<=20 and tipo=="A":
	total=(litros*al)
	desconto=total*(desA1/100)
	valorLiquido=total-desconto
	print(f'Valor a ser pago com descontos: {valorLiquido:.2f}')


if litros>20 and tipo=="A":
	total=(litros*al)
	desconto=total*(desA2/100)
	valorLiquido=total-desconto
	print(f'Valor a ser pago com descontos: {valorLiquido:.2f}')

if litros<=20 and tipo=="G":
	total=(litros*ga)
	desconto=total*(desG1/100)
	valorLiquido=total-desconto
	print(f'Valor a ser pago com descontos: {valorLiquido:.2f}')


if litros>20 and tipo=="G":
	total=(litros*ga)
	desconto=total*(desG2/100)
	valorLiquido=total-desconto
	print(f'Valor a ser pago com descontos: {valorLiquido:.2f}')


else:
	print('Combustivel invalido')
