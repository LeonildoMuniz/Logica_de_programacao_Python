for i in range(5):
	car=input('Digite o modelo do carro: ')
	marca.append(car)
	con=float(input('Digite o consumo do carro: '))
	consumo.append(con)
	vlr=con*g
	valor.append(vlr)
for i in range(5):
	for j in range(5):
		if consumo[i]>=consumo[j]:
			cont+=1
	if cont==5:
		menor=marca[i]
	cont=0
		

print()
print('='*50)
print('Relatorio Final:')
for i in range(5):
		print(f'{i+1} - {marca[i]} - {consumo[i]} - {1000/consumo[i]:.2f} litros - R$  {(1000/consumo[i])*g:.2f}')
print()
print(f'O menor consmo é do {menor}')



