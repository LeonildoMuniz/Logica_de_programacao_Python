vet1=[]
vet2=[]
vet3=[]
vetor=[]

for i in range(10):
	num=int(input(f'Vetor 1 Entre com o valor {i+1}: '))
	vet1.append(num)
print()
for i in range(10):
	num=int(input(f'Vetor 2 Entre com o valor {i+1}: '))
	vet2.append(num)
print()
for i in range(10):
	num=int(input(f'Vetor 3 Entre com o valor {i+1}: '))
	vet3.append(num)
print()
for i in range(10):
	vetor.append(vet1[i])
	vetor.append(vet2[i])
	vetor.append(vet3[i])

print(f'Valores vetor C: {vetor}')
