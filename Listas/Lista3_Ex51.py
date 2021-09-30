a=1
b=1
result=0
num=int(input('Informe o numeros de termos para serie: '))

for i in range(0,num,1):
	result+=a/b
	print(f'{i+1} - S = {a}/{b}')	
	b+=2
	a+=1


print(f'Soma total de serie: {result:.2f}')
