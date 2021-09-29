cont="A"
cont1=0
vet=[]
cont2=0
soma=0
num1=-1

while cont!="SAIR":
	while num1<0 or num1>1000:		
		num1=int(input(f'Informe o {cont1+1} numero: '))
		if num1<0 or num1>1000:
			print('Numero invalido, aceito somente entre 0 e 1000')
	vet.append(num1)
	soma+=num1
	cont1+=1
	cont=input('Digite SAIR para finalizar ou 1 para continuar: ')

for i in range(0,cont1):
	for j in range(0,cont1):
		if vet[i]>=vet[j]:
			cont2+=1
	if cont2==cont1:
		print()
		print('='*50)
		print(f'Maior numero: {vet[i]}')
	cont2=0

cont2=0
for i in range(0,cont1):
	for j in range(0,cont1):
		if vet[i]<=vet[j]:
			cont2+=1
	if cont2==cont1:
		print()
		print('='*50)
		print(f'Menor numero: {vet[i]}')
	cont2=0

print()
print('='*50)
print(f'Soma dos numeros digitados: {soma}')

