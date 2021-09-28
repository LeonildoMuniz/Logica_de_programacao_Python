a=int(input('Digite o valor de A: '))

if a==0:
	print('Valor de A = 0 equação não é de segundo grau')
else:
	b=int(input('Digite o valor de B: '))
	c=int(input('Digite o valor de C: '))
	delta= (b**2)-(4*a*c)
	if delta<0:
		print('Equação não possui raízes reais')
	if delta==0:
		print('Equação possui apenas uma raiz real')
		x=(-b+(delta))/(2*a)
		print(f'Valor da raiz de X: {x:.2f}')
	if delta>0:
		print('Equação possui duas raizes real')
		x1=(-b+(delta))/(2*a)
		x2=(-b-(delta))/(2*a)
		print(f'Valor de X1={x1:.2f} e X2={x2:.2f}')
