n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))

media=(n1+n2)/2

print()
print('='*50)
print()

if media<=4:
	print(f'Notas obitidas N1 = {n1:.2f}, N2 = {n2:.2f}')
	print(f'Media das notas: {media:.2f}')
	print('Entre 4.0 e zero - Conceito: E')
	print('Reprovado!')

if media>4 and media<=6:
	print(f'Notas obitidas N1 = {n1:.2f}, N2 = {n2:.2f}')
	print(f'Media das notas: {media:.2f}')
	print('Entre 4.0 e 6 - Conceito: D')
	print('Reprovado!')

if media>6 and media<=7.5:
	print(f'Notas obitidas N1 = {n1:.2f}, N2 = {n2:.2f}')
	print(f'Media das notas: {media:.2f}')
	print('Entre 6 e 7.5 - Conceito: C')
	print('Aprovado!')

if media>7.5 and media<=9:
	print(f'Notas obitidas N1 = {n1:.2f}, N2 = {n2:.2f}')
	print(f'Media das notas: {media:.2f}')
	print('Entre 7.5 e 9 - Conceito: B')
	print('Aprovado!')

if media>9 and media<=10:
	print(f'Notas obitidas N1 = {n1:.2f}, N2 = {n2:.2f}')
	print(f'Media das notas: {media:.2f}')
	print('Entre 9 e 10 - Conceito: A')
	print('Aprovado!')
