n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
n3=float(input('Digite a terceira nota: '))

media=(n1+n2+n3)/3

if media==10:
	print(f'Aprovado com Distinção media: {media:.2f}')
if media>=7 and media<10:
	print(f'Aprovado media: {media:.2f}')
if media<7:
	print(f'Reprovado media: {media:.2f}')
