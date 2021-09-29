salto=[]
sair=1
total=0
cont=0
nam=0

while sair!="":
	nome=input('Atleta: ')
	if nome!="":
		nam=nome
	if nome=="":
		sair=""
	else:
		for i in range(7):
			s1=float(input(f'Nota {i+1}: '))
			salto.append(s1)
			total+=s1
		for i in range(7):
			for j in range(7):
				if salto[i]>=salto[j]:
					cont+=1
			if cont==7:
				print()
				print(f'Melhor nota: {salto[i]}')
				total-=salto[i]
			cont=0
		for i in range(7):
			for j in range(7):
				if salto[i]<=salto[j]:
					cont+=1
			if cont==7:
				print()
				print(f'Pior nota: {salto[i]}')
				total-=salto[i]
			cont=0
print(f'Media das notas: {total/5:.2f}')
print()
print('Resultado final:')
print(f'{nam} : {total/5:.2f}')
