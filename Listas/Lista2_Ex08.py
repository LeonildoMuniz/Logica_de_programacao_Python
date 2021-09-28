vl1 = float(input('Digite o primeiro valor: '))
vl2 = float(input('Digite o segundo valor: '))
vl3 = float(input('Digite o terceiro valor: '))

print()
print("*"*50)
print()


if vl1<vl2 and vl1<vl3:
	print(f'O produto mais barato custa R$ {vl1:.2f}')	

if vl2<vl1 and vl2<vl3:
	print(f'O produto mais barato custa R$ {vl2:.2f}')	

if vl3<vl1 and vl3<vl2:
	print(f'O produto mais barato custa R$ {vl3:.2f}')	
