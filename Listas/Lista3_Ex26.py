a=0
b=0
c=0

eleitores=int(input('Digite o total de eleitores: '))

for i in range(eleitores):
	print()
	print('='*50)
	print(f'Eleitor {i+1} Digite seu voto:')
	print('1 - Para candidato A')
	print('2 - Para candidato B')
	print('3 - Para candidato C')
	opcao=int(input('Opçao: '))
	if opcao==1:
		a+=1
	if opcao==2:
		b+=1
	if opcao==3:
		c+=1

print()
print('='*50)
print(f'Total de votos candidato A: {a}')
print(f'Total de votos candidato B: {b}')
print(f'Total de votos candidato C: {c}')
