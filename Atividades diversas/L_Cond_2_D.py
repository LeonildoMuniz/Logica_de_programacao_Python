n1=0
n2=0
n3=0
n4=0
n5=0
media=0
exame=0


n1=int(input('Digite a primeira nota: '))
n2=int(input('Digite a segunda nota: '))
n3=int(input('Digite a terceira nota: '))
n4=int(input('Digite a quarta nota: '))

media=(n1+n2+n3+n4)/4

if media>=7:
	print("Aluno aprovado! media: ",media)

else:
	n5=int(input('Digite a nota do exame: '))
	exame=(media+n5)/2
	if exame>=5:
		print("Aluno aprovado média final: ",exame)
	else:
		print("Aluno reprovado média final: ",exame)
