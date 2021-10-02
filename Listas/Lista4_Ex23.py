usuario=["Alexandre","Anderson","Antonio","Carlos","Cesar","Rosemary"]
espaco=[0]*5
total=0

for i in range(6):
	print('1 - alexandre\
		  \n2 - anderson\
		  \n 3 - antonio\
		  \n 4 - carlos\
		  \n 5 - cesar\
		  \n 6 -rosemary\
		  ')
	us=int(input('Escolha o usuario para digitar o tamanho do arquivo: '))
	num=int(input('Digite a quantidade: '))
	if us==1:
		espaco[0]=(num/1024/1024)
		total+=(num/1024/1024)
	elif us==2:
		espaco[1]=(num/1024/1024)
		total+=(num/1024/1024)
	elif us==3:
		espaco[2]=(num/1024/1024)
		total+=(num/1024/1024)
	elif us==4:
		espaco[3]=(num/1024/1024)
		total+=(num/1024/1024)
	elif us==5:
		espaco[4]=(num/1024/1024)
		total+=(num/1024/1024)

print()
print(f'Espaço Total ocupado: {total:.2f} MB')
print(f'Espaço médio ocoupado: {total/5:.2f} MB')
