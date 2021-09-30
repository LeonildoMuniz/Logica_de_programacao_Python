vet=[]
vet2=[]


for i in range(10):
	num=int(input(f'Digite o {i+1} valor: '))
	vet.append(num)

for i in range(10,0,-1):
	vet2.append(vet[i-1])

print(vet2)
