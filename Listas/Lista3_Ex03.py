cont=0
while cont!=1:
	nome=input('Digite o nome: ')
	if len(nome)>=3:
		cont+=1
	else:
		print('Nome precisa ter mais de três caracteres')

cont=0
while cont!=1:
	idade=int(input('Digite a idade: '))
	if idade>=0 and idade<=150:
		cont+=1
	else:
		print('Idade precisa ser entre 0 e 150')

cont=0
while cont!=1:
	salario=float(input('Digite o salario: '))
	if salario>0:
		cont+=1
	else:
		print('Salario precisa ser mais que 0')

cont=0
while cont!=1:
	sexo=input('Digite o sexo F ou M: ')
	if sexo=="F" or sexo=="M":
		cont+=1
	else:
		print('Sexo precisa ser F ou M')

cont=0
while cont!=1:
	estadoCivil=input('Digite o estado civil S, C, V, D: ')
	if estadoCivil=="S" or estadoCivil=="C" or estadoCivil=="V" or estadoCivil=="D":
		cont+=1
	else:
		print('Estado civil precisa ser S, C, V, D')

	
