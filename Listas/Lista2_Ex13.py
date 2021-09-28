diasDaSemana=["Domingo","Segunda","Terça",\
			   "Quarta","Quinta","Sexta","Sabado"]


dia=int(input('Digite (1-Domingo, 2- Segunda, etc.): '))

print()
print('='*50)
print()

if dia>=0 and dia<=7:
	print(f'{dia} - {diasDaSemana[dia-1]}')
else:
	print('Valor inválido')
