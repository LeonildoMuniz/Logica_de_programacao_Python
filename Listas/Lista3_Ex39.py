vet=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
cont=0

for i in range(10):
	for j in range(1):
		vet[i][j]=int(input(f'Digite o código do {i+1} aluno:  '))
		vet[i][j+1]=int(input(f'Digite a altura do {i+1} aluno em cm:  '))

for i in range(10):
	for j in range(10):
		if vet[i][2]>=veto[j][2]:
			cont+=1
		if cont==10:
			print(f'Codigo do aluno mais alto: {vet[i][1]}, altura: {vet[i][2]}')
