jose=0
joao=0
pedro=0
maria=0
ana=0
nulo=0
branco=0
sair="a"
total=0



print('Legenda:\nDescrição   Código\
	  \nJose            1\
	  \nJoão            2\
	  \nPedro           3\
	  \nMaria           4\
	  \nAna             5\
	  \nNulo            6\
	  \nBranco          7\
')

while sair!="S":
	cod=input('\nDigite seu voto, para encerrar "S": ')
	if cod=="S":
		sair="S"
	else:
		codigo=int(cod)			
		if codigo==1:
			jose+=1
			total+=1
		if codigo==2:
			joao+=1
			total+=1
		if codigo==3:
			pedro+=1
			total+=1
		if codigo==4:
			maria+=1
			total+=1
		if codigo==5:
			ana+=1
			total+=1
		if codigo==6:
			nulo+=1
			total+=1
		if codigo==7:
			branco+=1
			total+=1

print()
print('='*50)
print(f'Apuração de votos: \n\
	  Jose:    {jose}\n\
	  Joao:    {joao}\n\
	  Pedro:   {pedro}\n\
	  Maria:   {maria}\n\
	  Ana:     {ana}\n\
	  Nulo:    {nulo}\n\
	  Branco:  {branco}\n\
	  % Nulo:  {nulo/total:.2f}\n\
	  % Branco:{branco/total:.2f}')
