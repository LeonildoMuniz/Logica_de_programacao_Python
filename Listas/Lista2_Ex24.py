num1=float(input('Digite o primeiro numero: '))
num2=float(input('Digite o segundo numero: '))

op=int(input('Opções: \n 1 - Soma\n 2 - Subtração\n 3 - Divisão\n 4 - Multiplicação\n Digite a opção: '))

if op==1 or op==2 or op==3 or op==4:
	soma=num1+num2
	sub=num1-num2
	div=num1/num2
	mult=num1*num2

	print()
	print('='*50)
	print()
	
	if op==1:
		decimal=round(soma)
		print(f'Valor da soma: {soma:.2f} \n')
		if soma%2==0:
			print('Par')
		else:
			print('Impar')
		if soma<0:
			print('Negativa')
		else:
			print('Positiva')
		if decimal==soma:
			print('Inteiro')
		else:
			print('Decimal')

	if op==2:
		decimal=round(sub)
		print(f'Valor da subtração: {sub:.2f} \n')
		if sub%2==0:
			print('Par')
		else:
			print('Impar')
		if sub<0:
			print('Negativa')
		else:
			print('Positiva')
		if decimal==sub:
			print('Inteiro')
		else:
			print('Decimal')

	if op==3:
		decimal=round(div)
		print(f'Valor da divisão: {div:.2f} \n')
		if div%2==0:
			print('Par')
		else:
			print('Impar')
		if div<0:
			print('Negativa')
		else:
			print('Positiva')
		if decimal==div:
			print('Inteiro')
		else:
			print('Decimal')

	if op==4:
		decimal=round(mult)
		print(f'Valor da multiplicação: {mult:.2f} \n')
		if mult%2==0:
			print('Par')
		else:
			print('Impar')
		if mult<0:
			print('Negativa')
		else:
			print('Positiva')
		if decimal==mult:
			print('Inteiro')
		else:
			print('Decimal')
				

else:
	print('Opção invalida!')
