a=1
b=2
result=0
num=int(input('Informe o numeros de termos para serie: '))

for i in range(0,num,1):
	result+=a+(a/b)
	print(f'{i+1} - H = {a}+{a}/{b}')	
	b+=1

print(f'Soma total de serie: {result:.2f}')
