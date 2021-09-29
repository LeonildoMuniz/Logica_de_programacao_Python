cQuente=1.20
bSimples=1.30
bOvo=1.50
ham=1.20
che=1.30
ref=1.00
sair="a"
valor1=0
valor2=0

print('Menu:\nEspecificação   Código  Preço\
	  \nCachorro Quente 100     R$ 1,20\
	  \nBauru Simples   101     R$ 1,30\
	  \nBauru com ovo   102     R$ 1,50\
	  \nHambúrguer      103     R$ 1,20\
	  \nCheeseburguer   104     R$ 1,30\
	  \nRefrigerante    105     R$ 1,00\
')

while sair!="S":
	cod=input('\nDigite o código do produto para sair digite "S": ')
	if cod=="S":
		sair="S"
	else:
		codigo=int(cod)			
		if codigo==100:
			quant=int(input('Digite a quantidade: '))
			valor1=quant*cQuente
			valor2+=valor1
			print('='*50)
			print(f'Valor do item: R$ {valor1:.2f}')
		if codigo==101:
			quant=int(input('Digite a quantidade: '))
			valor1=quant*bSimples
			valor2+=valor1
			print('='*50)
			print(f'Valor do item: R$ {valor1:.2f}')			
		if codigo==102:
			quant=int(input('Digite a quantidade: '))
			valor1=quant*bOvo
			valor2+=valor1
			print('='*50)
			print(f'Valor do item: R$ {valor1:.2f}')			
		if codigo==103:
			quant=int(input('Digite a quantidade: '))
			valor1=quant*ham
			valor2+=valor1
			print('='*50)
			print(f'Valor do item: R$ {valor1:.2f}')			
		if codigo==104:
			quant=int(input('Digite a quantidade: '))
			valor1=quant*che
			valor2+=valor1
			print('='*50)
			print(f'Valor do item: R$ {valor1:.2f}')			
		if codigo==105:
			quant=int(input('Digite a quantidade: '))
			valor1=quant*ref
			valor2+=valor1	
			print('='*50)
			print(f'Valor do item: R$ {valor1:.2f}')

print('='*50)
print(f'Total a pagar: R$ {valor2:.2f}')
