result=1
num1=int(input('Digite o numero para calular o fatorial: '))

for i in range(0,num1):
	result=result+result*i

print(f'Fatorial do numero infomardo: {result}')
