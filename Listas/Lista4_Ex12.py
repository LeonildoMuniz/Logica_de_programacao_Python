alunos=3
idade=[]
altura=[]
media=0
soma=0
cont=0
for i in range(alunos):
	print(f'Aluno {i+1}:')
	num=(int(input('Informe sua idade: ')))
	idade.append(num)
	num2=0
	num2=(int(input('Informe sua altura: ')))
	altura.append(num2)
	print()
	soma+=num2
media=soma/alunos
print(f'Media da altura dos alunoa {media:.2f} cm.')

for i in range(alunos):
	if idade[i]>13 and altura[i]<media:
		cont+=1
print(f'{cont} aluno(s) com mais de 13 anos e altura abaixo da media.')
