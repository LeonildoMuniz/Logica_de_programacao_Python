sair=0
cont=0
result=0
while sair!="S":
	num=input(f'Digite o {cont+1} numero, se desejar sair digite "S":  ')
	cont+=1
	if num!="S":
		result+=int(num)
	else:
		sair=num	

print(f'Media dos valores digitados: {result/(cont-1)}')
