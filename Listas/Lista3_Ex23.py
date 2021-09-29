cont=0
vet=[]
vet2=[]
cont2=0
num1=int(input('Verificar numeros primos do intervano 1 a : '))

for i in range(num1):
	vet.append(i+1)


for i in range(0,num1):
	for j in range(0,num1):
		cont2+=1
		if vet[i]%(j+1)==0:
			cont+=1
	
	if cont == 2:
		vet2.append(vet[i])
	cont=0

print()
print('='*50)
print(f'Numeros primos encontrados:\n {vet2}')
print()
print('='*50)
print(f'Numero de divisões realizadas: {cont2}')
