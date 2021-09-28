dia=int(input('Digite o dia: '))
mes=int(input('Digite o mês: '))
ano=int(input('Digite o ano: '))

if dia>=1 and dia <=31 and mes>=1 and mes<=12 and ano>=1:
	if mes==4 or mes==6 or mes==9 or mes==11 or mes==2:
		if dia > 30:
			print('Data digitada inválida')
		if mes==2 and dia>28 and ano%4!=0:
			print('Data digitada inválida')
		if mes==2 and dia>29 and ano%4==0:
			print('Data digitada inválida')
		else:
			print('Data válida')
	else:
		print('Data válida!')

			

else:
	print('Data digitada inválida')
