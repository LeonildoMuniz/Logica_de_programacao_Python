num1=1
while num1<16:
	result=1
	num1=int(input('Caculo de fatorial maximo 16 para fechar: '))
	
	for i in range(0,num1):
		result=result+result*i
	
	print(f'Fatorial do numero infomardo: {result}')
