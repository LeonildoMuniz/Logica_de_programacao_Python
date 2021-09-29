anos=0
cont=0
populacaoA=80000
populacaoB=200000

while cont!=1:
	populacaoA+=populacaoA*0.03
	populacaoB+=populacaoB*0.015
	if populacaoA<=populacaoB:
		anos+=1
	else:
		print(f'Anos necessario para população A passar população B: {anos} anos')
		print(f'Total população A: {populacaoA:.0f}')
		print(f'Total população B: {populacaoB:.0f}')
		cont+=1
