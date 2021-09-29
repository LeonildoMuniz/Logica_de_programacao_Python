num=[0,0,0,0,0]
cont=0

for i in range(0,5):
	num[i]=int(input(f'Digite o {i+1} valor: '))

for i in range(0,5):
	for j in range(0,5):
		if num[i] >= num[j]:
			cont+=1
	if cont==5:
		print(f'Maior numero digitado {num[i]}')
	cont=0
