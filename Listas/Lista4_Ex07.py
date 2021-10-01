vetor = []
soma = 0
mult = 1

for i in range(5):
	num=(int(input(f'Digite o numero {i+1}: ')))
	vetor.append(num)
	soma+=num
	mult*=num

print()
print(f'A soma dos valores: {soma}')
print(f'A multiplicacao dos valores: {mult}')
print(f'Os valores informados: {vetor}')
