quant=[0]*5
cont=0
sair=1
lista=['necessita da esfera','necessita de limpeza','necessita troca do cabo ou conector','quebrado ou inutilizado']
while sair!=0:
	qb=int(input('Informe o defeito:\n1- necessita da esfera\
			 \n2- necessita de limpeza\
			 \n3- necessita troca do cabo ou conector\
			 \n4- quebrado ou inutilizado\
			 \n0 - sair\
			 \nOpção: '))

	if qb==0:
		sair=0
	elif qb<0 or qb>4:
		print('Opção invalida')
	elif qb==1:
		quant[0]+=1
		cont+=1
	elif qb==2:
		quant[1]+=1
		cont+=1
	elif qb==3:
		quant[2]+=1
		cont+=1
	elif qb==4:
		quant[3]+=1
		cont+=1
	elif qb==5:
		quant[4]+=1
		cont+=1


print()
print('='*50)
print(f'Quantidade e mouses: {cont}')

for i in range(cont):
	print(f'{lista[i]} - quantidade {quant[i]} - {quant[i]/cont*100:.2f}%')

	
	
