sair="a"
cont=0
cont2=0
vet=[]
total=0

while sair!="S":
	temp=input('Digite a temperatura, para sair digite "S": ')

	if temp=="S":
		sair="S"
	else:
		vet.append(int(temp))
		total+=int(temp)
		cont+=1

print()
print('='*50)

for i in range(cont):
	for j in range(cont):
		if vet[i]<=vet[j]:
			cont2+=1

		if cont2==cont:
			print(f'Menor temperatura: {vet[i]}')
	cont2=0

for i in range(cont):
	for j in range(cont):
		if vet[i]>=vet[j]:
			cont2+=1

		if cont2==cont:
			print(f'Maior temperatura: {vet[i]}')
	cont2=0

print(f'Media das temperaturas informadas: {total/cont:.2f}')
