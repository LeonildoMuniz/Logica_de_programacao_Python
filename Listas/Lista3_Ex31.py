preco=1
cont=0
total=0
print('Lojas Tabajara')
while preco!=0:
	produto=float(input(f'Produto {cont+1}: R$ '))
	cont+=1
	if produto==0:
		preco=produto
	else:
		total+=produto

print(f'Total: R$ {total:.2f}')
dinheiro=float(input('Dinheiro: R$ '))

print(f'Troco: R$ {dinheiro-total:.2f}')
