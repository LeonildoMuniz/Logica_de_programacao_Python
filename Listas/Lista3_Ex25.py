sair=0
cont=0
result=0
media=0
while sair!="S":
	num=input(f'Digite a {cont+1} idade, se desejar sair digite "S":  ')
	cont+=1
	if num!="S":
		result+=int(num)
	else:
		sair=num	

media=result/(cont-1)

if media>=0 and media<=25:
	print()
	print('='*50)
	print(f'Turma jovem media de idade: {media:.2f}')

if media>25 and media<=60:
	print()
	print('='*50)
	print(f'Turma adulta media de idade: {media:.2f}')

if media>60:
	print()
	print('='*50)
	print(f'Turma idosa media de idade: {media:.2f}')
