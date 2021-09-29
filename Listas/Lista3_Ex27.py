soma=0
cont=0

turmas=int(input('Digite o total de turmas: '))

for i in range(turmas):
	print()
	print('='*50)
	alunos=int(input(f'Turma {i+1} digite o total de alunos : '))
	
	while alunos>40:
		alunos=int(input('Turma não pode ter mais que 40 alunos digite novamente: '))

	cont+=1
	soma+=alunos


print()
print('='*50)
print(f'Media de alunos das turmas: {soma/(cont-1):}')
