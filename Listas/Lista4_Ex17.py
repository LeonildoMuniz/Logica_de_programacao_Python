sair="a"
nome=[]
list=["Primeiro","Segundo","Terceiro","Quarto","Quinto"]
salto=[0]*5
salto2=[0]*50
result=0
cont=0
media=[]

while sair!="":
	a=input('\nAtleta: ')
	if a=="":
		sair=""
	elif a!="":
		nome.append(a)
		for i in range(5):
			salto[i]=float(input(f'{list[i]} Salto: '))
			result+=salto[i]
	
		cont+=1		
		salto2[cont-1]=salto
		media.append(result/5)
		result=0
		salto=[0]*5


for i in range(cont):
	print()
	print('='*50)
	print('Resultado Final:')
	print(f'Atleta: {nome[i]}')
	print(f'Saltos: {salto2[i]}')
	print(f'Média dos saltos: {media[i]:.2f}')
