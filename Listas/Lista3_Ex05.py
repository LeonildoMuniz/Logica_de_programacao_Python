anos=0
cont=0
cont2=0
import os


while cont2!=1:
	populacaoA=float(input('Digite a populaçao A: '))
	taxaA=float(input('Digite a taxa de crescimento população A:'))
	populacaoB=float(input('Digite a populaçao b: '))
	taxaB=float(input('Digite a taxa de crescimento população B:'))

	while cont!=1:
		populacaoA+=populacaoA*(taxaA/100)
		populacaoB+=populacaoB*(taxaB/100)

		if populacaoA<=populacaoB:
			anos+=1
		else:
			print()
			print('='*50)
			print()
			print(f'Anos necessario para população A passar população B: {anos} anos')
			print(f'Total população A: {populacaoA:.0f}')
			print(f'Total população B: {populacaoB:.0f}')
			cont+=1
			print()
			print('='*50)
			print()

		if populacaoA>=populacaoB:
			anos+=1
		else:
			print()
			print('='*50)
			print()
			print(f'Anos necessario para população A passar população B: {anos} anos')
			print(f'Total população A: {populacaoA:.0f}')
			print(f'Total população B: {populacaoB:.0f}')
			cont+=1
			print()
			print('='*50)
			print()

				
	cont2=int(input('Para outro caculo digite 0 para encerrar 1: '))

		
