reajuste=1.5
ano=2021
ano1=1996
salReajuste=0

salInicial=float(input('Digite o salario atual: '))

salReajuste=salInicial*(1+(reajuste/100))

for i in range(ano1+1,ano,1):
	reajuste*=2
	salReajuste*=(1+(reajuste/100))

print(f'Salario atual: {salReajuste:.2f}')
