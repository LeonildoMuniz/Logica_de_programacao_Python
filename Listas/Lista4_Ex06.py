media = []
cont = 0
for i in range(10):
	soma = 0
	for j in range(4):
		nota = float(input(f'Entre com a nota {j+1} do aluno {i+1}: '))
		soma+=nota
	media.append(soma/4)
	print()

for i in range(10):
	print(f'A nota madia do aluno {i+1}: {media[i]}')	
	if media[i]>=7:
		cont+=1
print()	
print(f'{cont} aluno(s) com media maior ou igual a 7.0')
