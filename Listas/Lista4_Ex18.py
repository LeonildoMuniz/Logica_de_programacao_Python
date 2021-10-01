sair=1
cont=0
cont2=0
voto=[]
apuracao=[0]*23


while sair!=0:
	num=int(input('Número do jogador (0=fim): '))
	if num==0:
		sair=0
	elif num<0 or num>23:
		print('Digite novamente numero invalido')
	else:
		voto.append(num)
		cont+=1

for i in range(cont):
	for j in range(23):
		if voto[i]==j:
			apuracao[j]+=1
print()
print('='*50)
print('Resultado da votação:')
print()
print(f'Foram apurados {cont} votos.')

for i in range(23):
	if apuracao[i]!=0:
		print(f'Jogador {i} = {apuracao[i]} votos com {(apuracao[i]/cont*100):.2f}%')

for i in range(23):
	for j in range(23):
		if apuracao[i]>apuracao[j]:
			cont2+=1
	if cont2==21:
		print(f'O melhor jogador foi o número {i}, com {apuracao[i]} votos, correspondendo a {(apuracao[i]/cont*100):.2f}% do total de votos.')
	cont=0
