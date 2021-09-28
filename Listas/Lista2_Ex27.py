morangoP1=2.5
morangoP2=2.2
macaP1=1.8
macaP2=1.5
des=10


morango=float(input('Digite o peso do morango: '))
maca=float(input('Digite o peso do maçã: '))

peso=morango+maca

if peso>=8:
	if morango>=5:
		totalMorango=morango*morangoP1
	else:
		totalMorango-morango*morangoP2

	if maca>=5:
		totalMaca=maca*macaP1
	else:
		totalMaca-maca*macaP2

	vlrBruto=totalMaca+totalMorango
	vlrLiquido=vlrBruto-(vlrBruto*(des/100))

	print()
	print('='*50)
	print()
	print(f'Valor total a pagar: R$ {vlrLiquido:.2f}')


else:
	totalMaca=maca*macaP1
	totalMorango=morango*morangoP1
	vlrBruto=totalMaca+totalMorango

	print()
	print('='*50)
	print()
	print(f'Valor total a pagar: R$ {vlrBruto:.2f}')

