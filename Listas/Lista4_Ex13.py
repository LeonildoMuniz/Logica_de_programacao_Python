temp=[]
acima=[]
soma=0
media=0
mes=[]

for i in range(12):
	vl1=input('Informe o mes por extenso: ')
	mes.append(vl1)
	vl2=float(input('Informe a temperatura: '))
	temp.append(vl2)
	soma+=vl2
media=soma/12
print()
for i in range(12):
	if temp[i]>media:
		acima.append(temp[i])
		print(f'{i+1} - {mes[i]} Temperatura: {temp[i]}')
