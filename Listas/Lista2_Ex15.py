triangulo=[0,0,0]
cont=0

while cont<3:
	triangulo[cont]=float(input(f'Digite o {cont+1} lado do triangulo: '))
	cont+=1

cont=0

for i in range(0,3):
	if triangulo[i]>0:
		cont+=1


if cont>=1:
	print('Valores informados podem ser um triangulo!')
	print()
	print('='*50)
	print()
	cont=0
	for i in range (0,3):
		for j in range(0,3):
			if triangulo[i]>triangulo[j]:
				cont+=1
	if cont == 0:
		print('Triângulo Equilátero')
	if cont == 2:
		print('Triângulo Isósceles')
	if cont == 3:
		print('Triângulo Escaleno')

	
else:
	print()
	print('='*50)
	print()
	print('Valores informados não podem ser um triangulo!')
	
	
