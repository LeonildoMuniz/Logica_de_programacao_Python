cont=0
maior=0
n=[[0],[0],[0]]
n2=[[0],[0],[0]]
while cont<3:
	n[cont] = int(input(f'Ditite o {cont+1} valor: '))
	cont+=1

for i in range(0,3):
	for j in range(0,3):
		if n[i]>n[j]:
			maior+=1

	n2[maior] = n[i]

	maior=0

print(n2)
