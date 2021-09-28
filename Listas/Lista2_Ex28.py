fileP1=4.9
fileP2=5.8
alcatraP1=5.9
alcatraP2=6.8
picanhaP1=6.9
picanhaP2=7.8
des=5

tipo=int(input('Escolha o tipo de carne:\n\
 1-File\n 2-Alcatra\n 3-Picanha\n Digite a opção: '))
quantidade=int(input('Digite a quantidade de kg: '))

print()
print('='*50)
print()

if tipo==1 or tipo==2 or tipo==3:
	pag=int(input('1-Cartão Tabajara\n2-Outros\nEscolha a opção: '))

	print()
	print('='*50)
	print()

	if pag==1 and quantidade>=5:
		valor=quantidade*fileP1
		valorLiquido=valor-(valor*(des/100))
		print(f'Produto: File')
		print(f'Desconto cartão Tabajara:{valor*(des/100):.2f} ')
		print(f'Valor liquido: R$ {valorLiquido:.2f}')
	if pag==1 and quantidade<5:
		valor=quantidade*fileP2
		print(f'Produto: File')
		print(f'Valor a pagar: R$ {valor:.2f}')

	if pag==2 and quantidade>=5:
		valor=quantidade*alcatraP1
		valorLiquido=valor-(valor*(des/100))
		print(f'Produto: Alcatra')
		print(f'Desconto cartão Tabajara:{valor*(des/100):.2f} ')
		print(f'Valor liquido: R$ {valorLiquido:.2f}')
	if pag==2 and quantidade<5:
		valor=quantidade*alcatraP2
		print(f'Produto: Alcatra')
		print(f'Valor a pagar: R$ {valor:.2f}')

	if pag==3 and quantidade>=5:
		valor=quantidade*picanhaP1
		valorLiquido=valor-(valor*(des/100))
		print(f'Produto: Picanha')
		print(f'Desconto cartão Tabajara:{valor*(des/100):.2f} ')
		print(f'Valor liquido: R$ {valorLiquido:.2f}')
	if pag==3 and quantidade<5:
		valor=quantidade*picanhaP2
		print(f'Produto: Picanha')
		print(f'Valor a pagar: R$ {valor:.2f}')



else:
	print('Opção invalida!')
