anos=0
cont=0
cont2=0


while cont2!=1:
	populacaoA=float(input('Digite a populaçao A: '))
	taxaA=float(input('Digite a taxa de crescimento população A: '))
	populacaoB=float(input('Digite a populaçao B: '))
	taxaB=float(input('Digite a taxa de crescimento população B: '))
	if populacaoA>populacaoB and taxaA>taxaB or populacaoA<populacaoB and taxaA<taxaB:
		print('Não há como uma população alcançar a outra devido a maior taxa ser da maior população!')
	else:	
		if populacaoA<=populacaoB:
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
			while cont!=1:
				populacaoA+=populacaoA*(taxaA/100)
				populacaoB+=populacaoB*(taxaB/100)
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
		cont2=2
		cont=0
		anos=0
		
