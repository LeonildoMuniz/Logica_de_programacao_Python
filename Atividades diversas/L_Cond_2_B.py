A=0
B=0
C=0
delta=0
x1=0
x2=0

A=int(input('Digite o valor de A: '))
B=int(input('Digite o valor de B: '))
C=int(input('Digite o valor de C: '))

delta=(B**2)-(4*A*C)
delta=delta**0.5


if delta<0:
	print("Não existe raiz real para delta = ",delta)

if delta>=0:
	x1=((-B-delta)/(2*A))
	x2=((-B+delta)/(2*A))
	print("Valor de X1 = ",x1)	
print("Valor de X2 = ",x1)

