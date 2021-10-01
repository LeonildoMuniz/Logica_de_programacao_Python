vetor = []
soma=0
for i in range(4):
	nota=(float(input(f'Digite a nota {i+1}: ')))
	vetor.append(nota)
	soma+=nota
print(f'As notas foram: {vetor}')
print(f'A média das notas: {soma/4}')
