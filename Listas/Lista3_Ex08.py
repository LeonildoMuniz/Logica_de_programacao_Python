soma=0

for i in range (0,5):
	num=int(input(f'Digite o {i+1} valor:  '))
	soma+=num

print(f'Média dos numeros digitados {soma/5}')
