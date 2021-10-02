vet=[]
import random
cont=0

for i in range(100):
	x = random.randint(1,6)
	vet.append(x)

print()
print('='*50)
print('Resultado dos 100 lançamentos:')
for i in range(6):
	for j in range(100):
		if vet[i] == vet[j]:
			cont+=1
	print(f'Dado na posiçao {i+1} = {cont} vezes sorteado')
	cont=0
