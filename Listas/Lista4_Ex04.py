vet=[]
vet2=[]
cont=0

for i in range(10):
	num=input(f'Digite o {i+1} caracter: ')
	vet.append(num)

for i in range(10):
	if vet[i]!="a" and vet[i]!="e"and\
	vet[i]!="i"and vet[i]!="o"and vet[i]!="u":
		vet2.append(vet[i])
		cont+=1
print(f'Total de consoantes: {cont}: \n{vet2}')
