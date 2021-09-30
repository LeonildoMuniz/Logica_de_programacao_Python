sair=1
vet=[]
vet2=[]
cont=0

while sair>=0:
	num=int(input(f'Digite o {cont+1} valor, valores negativos: '))

	if num<0:
		sair=num
	else:
		vet.append(num)
		cont+=1

for i in range(cont,0,-1):
	vet2.append(vet[i-1])

print(vet2)
