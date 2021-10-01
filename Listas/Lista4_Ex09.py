vetor = []
result = 0
for i in range(10):
	num = int(input(f'Entre com o número {i+1}: '))
	vetor.append(num)
	result+=num*2
print()
print(f'A soma do quadrado dos valores informados: {result}')
