cont=0

while cont!=1:
	nome=input('Digite o seu login: ')
	senha=input('Digite sua senha: ')
	
	if nome==senha:
		print('Senha e login não podem ser iguais')
	else:
		print('Senha e login aceitos!')
		cont+=1
