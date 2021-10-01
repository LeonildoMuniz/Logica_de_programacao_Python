idade = []
altura = []

for i in range(5):
	vl1=(int(input(f'Informe a idade da pessoa {i+1}: ')))
	idade.append(vl1)
	vl2=(float(input(f'Informe a altura da pessoa {i+1}: ')))
	altura.append(vl2)
print()
for i in range(5,0,-1):
	print(f'Pessoa {i}. tem {idade[i-1]} anos e mede {altura[i-1]}')

