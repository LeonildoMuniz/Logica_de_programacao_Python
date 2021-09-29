vet=[]


for i in range(0,10):
	num1 = int(input(f'Informe o {i+1} valor: '))
	vet.append(num1)

print()
print('='*50)
print('Numeros pares:\n')
for i in range(0,10):
	if vet[i]%2==0:
		print(vet[i])

print()
print('='*50)
print('Numeros impares:\n')
for i in range(0,10):
	if vet[i]%2!=0:
		print(vet[i])
