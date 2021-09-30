cont="0"
cont1=0
vet=[]
maior=[]
menor=[]
cont2=0
soma=0
media=0

while cont!="-1":
	num1=float(input(f'Informe a {cont1+1} nota: '))
	vet.append(num1)
	soma+=num1
	cont1+=1
	cont=input('Digite -1 para finalizar ou 0 para continuar: ')

media=soma/cont1

print('='*50)
print(f'Quantidade de notas lidas: {cont1}')
print()
print('='*50)

print(f'Notas lidas: {vet}')
print()
print('='*50)

for i in range(cont1,0,-1):
	print(f'Notas lidas em ordem inversa: {vet[i-1]}')
	cont1-+1

print()
print('='*50)
print(f'Soma das notas digitadas: {soma}')

print()
print('='*50)
print(f'Media das notas digitadas: {media:.2f}')

for cont2 in range(0,cont1):
	if vet[cont2]>media:
		maior.append(vet[cont2])
		cont2+=1
	else:
		menor.append(vet[cont2])
		cont2+=1

print()
print('='*50)
print(f'Notas acima da media: {maior}')

print()
print('='*50)
print(f'Notas abaixo da media: {menor}')

print()
print('='*50)

print("Calculo finalizado.")
