A=0
B=0
C=0

A=int(input('Digite o valor de A: '))
B=int(input('Digite o valor de B: '))
C=int(input('Digite o valor de C: '))

if C>B:
	if B>A:
		print(A)
		print(B)
		print(C)
if B>C:
	if C>A:
		print(A)
		print(C)
		print(B)	
if C>A:
	if A>B:
		print(B)
		print(A)
		print(C)
if A>C:
	if C>B:
		print(B)
		print(C)
		print(A)
if B>A:
	if A>C:
		print(C)
		print(A)
		print(B)	
if A>B:
	if B>C:
		print(C)
		print(B)
		print(A)	
