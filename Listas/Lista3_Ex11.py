cont=0
cont1=0
soma=0

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num2<num1:
	a=num2
	num2=num1
	num1=a

while cont!=1:
		if num1<=num2:
			print(num1)
			soma+=num1
			num1+=1

		else:
			cont=+1
print(f'Soma dos numeros: {soma}')	
