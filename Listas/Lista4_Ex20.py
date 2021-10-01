
sair=1
cont=0
cont2=0
cont3=0
abono=[]
salario=[]
total=0
maior=0


while sair!=0:
	num=int(input('Salario: '))
	if num==0:
		sair=0
	elif (num*0.2)<=100:
		abono.append(100)
		salario.append(num)
		cont+=1
	else:
		abono.append(num*0.2)
		salario.append(num)
		cont+=1

print()
print('='*50)

for i in range(cont):
	print(f'Salario: {salario[i]} - Abono: {abono[i]:.2f}')
	if abono[i]==100:
		cont2+=1
		total+=abono[i]
	for j in range(cont):
		if abono[i]>=abono[j]:
			cont3+=1
	if cont3==cont:
		maior=abono[i]
	cont3=0

print()
print(f'Foram processados {cont} colaboradores\
	  \nTotal gasto com abonos: R$ {total:.2f}\
	  \nValor mínimo pago a {cont2} colaboradores\
	  \nMaior valor de abono pago: R$ {maior:.2f}')
