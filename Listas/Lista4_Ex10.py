vetA=[]
vetB=[]
vetC=[]

for i in range(10):
	num=int(input(f'Vetor A Entre com o valor {i+1}: '))
	vetA.append(num)
print()
for i in range(10):
	num=int(input(f'Vetor B Entre com o valor {i+1}: '))
	vetB.append(num)
print()
for i in range(10):
	vetC.append(vetA[i])
	vetC.append(vetB[i])

print(f'Valores vetor C: {vetC}')
