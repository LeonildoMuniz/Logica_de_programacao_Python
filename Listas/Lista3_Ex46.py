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
		for i in range(5):
			s1=float(input(f'Digite o {i+1} salto: '))
			salto.append(s1)
			total+=s1
		for i in range(5):
			for j in range(5):
				if salto[i]>=salto[j]:
					cont+=1
			if cont==5:
				print()
				print(f'Melhor salto: {salto[i]}')
				total-=salto[i]
			cont=0
		for i in range(5):
			for j in range(5):
				if salto[i]<=salto[j]:
					cont+=1
			if cont==5:
				print()
				print(f'Pior salto: {salto[i]}')
				total-=salto[i]
			cont=0
print(f'Media dos demais saltos: {total/3:.2f}')
print()
print('Resultado final:')
print(f'{nam} : {total/3:.2f}')
