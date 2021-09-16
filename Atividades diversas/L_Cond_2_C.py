n1=0
n2=0
n3=0
n4=0
media=0


n1=int(input('Digite a primeira nota: '))
n2=int(input('Digite a segunda nota: '))
n3=int(input('Digite a terceira nota: '))
n4=int(input('Digite a quarta nota: '))

media=(n1+n2+n3+n4)/4

if media>=5:
	print("Aluno aprovado! media: ",media)

else:
	print("Aluno reprovado! media: ",media)


