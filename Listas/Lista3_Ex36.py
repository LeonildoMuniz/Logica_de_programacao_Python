a=0
num=int(input('Montar a tabuada de: '))
num2=int(input('Começar por: '))
num3=int(input('Terminar em: '))

if num2>num3:
	a=num3
	num3=num2
	num2=a

print()
print(f'Vou montar a tabuada de {num} começando em {num2} e terminando em {num3}:')


for i in range(num2,num3+1):
	print(f'{num} x {i} = {num*i}')
