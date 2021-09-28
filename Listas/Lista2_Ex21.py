cont1=0
cont2=0
cont3=0
cont4=0

saque=int(input('Digite o valor para o saque entre R$ 10,00 e R$ 600,00 : '))
saqueTotal=saque

print()
print('='*50)
print()

if saque>=10 and saque<=600:
	while saque>99:
		saque-=100
		cont1+=1
		
	if cont1>0:
		print(f'{cont1} - Notas separa(s) de: R$ 100,00 valor R$ {100*cont1:.2f}')

		
	while saque>49:
		saque-=50
		cont2+=1

	if cont2>0:
		print(f'{cont2} - Nota(s) separa(s) de: R$ 50,00 valor R$ {50*cont2:.2f}')
		
	while saque>9:
		saque-=10
		cont3+=1

	if cont3>0:
		print(f'{cont3} - Nota(s) separa(s) de: R$ 10,00 valor R$ {10*cont3:.2f}')

	while saque>4:
		saque-=5
		cont4+=1

	if cont4>0:
		print(f'{cont4} - Nota(s) separa(s) de: R$ 5,00 valor R$ {5*cont4:.2f}')

	if saque>0:
		print(f'{saque} - Nota(s) separa(s) de: R$ 1,00 valor R$ {saque:.2f}')

	print()
	print('='*50)
	print()
	print(f'Valor total sacado: R$ {saqueTotal:.2f}')

else:
	print()
	print('='*50)
	print()
	print('Valor digitado não pode se sacado!')

