cd=0
sair="A"
quant=0
valor=0
cont=0

	
while sair!="S":
	op=input('Infome a quantidade de CD''s para sair digite "S": ')
	if op=="S":
		sair=op;
	else:
		cd=int(op)
		for i in range(cd):
			preco=int(input(f'Digite o valor do {i+1} CD: '))
			valor+=preco
			cont+=1
	sair="S"


if sair!="S":
	print()
	print('='*50)
	print(f'Valor total invetido: {valor}')
	print(f'Media gasta por CD: {valor/(cont):.2f}')
