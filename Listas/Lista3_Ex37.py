sair=1
cont=0
cont2=0
cod=[]
alt=[]
pes=[]
pesTotal=0
altTotal=0

while sair!=0:
	codigo=int(input('Digite seu código, para sair digite 0: '))

	if codigo==0:
		sair=0
	else:
		altura=float(input('Digite sua altura: '))
		peso=float(input('Digite seu peso: '))			
		cod.append(codigo)
		alt.append(altura)
		pes.append(peso)
		pesTotal+=peso
		altTotal+=altura
		cont+=1



print()
print('='*50)

for i in range(cont):
	for j in range(cont):
		if alt[i]<=alt[j]:
			cont2+=1

		if cont2==cont:
			print('='*50)
			print(f'Código mais baixo: {cod[i]}')			
			print(f'Mais baixo: {alt[i]}')
	cont2=0

for i in range(cont):
	for j in range(cont):
		if alt[i]>=alt[j]:
			cont2+=1

		if cont2==cont:
			print('='*50)
			print(f'Código mais Alto: {cod[i]}')			
			print(f'Mais alto: {alt[i]}')
	cont2=0

for i in range(cont):
	for j in range(cont):
		if pes[i]<=pes[j]:
			cont2+=1

		if cont2==cont:
			print('='*50)
			print(f'Código mais magro: {cod[i]}')			
			print(f'Mais gordo: {pes[i]}')
	cont2=0

for i in range(cont):
	for j in range(cont):
		if pes[i]>=pes[j]:
			cont2+=1

		if cont2==cont:
			print('='*50)			
			print(f'Código mais gordo: {cod[i]}')			
			print(f'Mais magro: {pes[i]}')
	cont2=0

print('='*50)
print(f'Media de pesos: {pesTotal/cont:.2f}')
print(f'Media de alturas: {altTotal/cont:.2f}')





