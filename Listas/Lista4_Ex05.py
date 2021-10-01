vetor = []
par = []
impar = []
cont=0
cont2=-1

print('Digite 20 numeros inteiros.')

for i in range(20):
	num=int(input(f'Digite o numero {i+1}: '))
	vetor.append(num)
	cont+=1

for i in range(20):
	if vetor[i]%2==0:
		par.append(vetor[i])
	else:
		impar.append(vetor[i])

print(f'\nOs numeros informados foram: {vetor}')
print(f'\nOs numeros pares foram: {par}')
print(f'\nOs numeros impares foram: {impar}')
