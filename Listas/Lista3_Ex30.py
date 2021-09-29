
preco=float(input('Preço do pão: '))
print('Panificadora Pão de Ontem - Tabela de preços')
for i in range(50):
	print(f'{i+1} - R$ {preco*(i+1):.2f}')
