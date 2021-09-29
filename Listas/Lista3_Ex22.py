cont=0
vet=[]
cont2=0
num1=int(input('Informe o numero para verificar se é primo: '))
	
for i in range(0,num1):
	if num1%(i+1)==0:
		cont+=1
		cont2=i+1
		vet.append(cont2)

if cont == 2:
	print(f'Numero infomardo: {num1} é primo')
else:
	print(f'Numero infomardo: {num1} é par divisivel por {vet}')
