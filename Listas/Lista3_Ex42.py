sair=1
cont=0
vet=[]
a=0
b=0
c=0
d=0

while sair>=0:
	num=int(input(f'Digite o {cont+1} numero, negativo encerra: '))
	if num<0:
		sair=-1
	else:
		vet.append(num)
		cont+=1

for i in range(cont):
	if vet[i]>=0 and vet[i]<26:
		a+=1
	if vet[i]>=26 and vet[i]<=50:
		b+=1
	if vet[i]>=51 and vet[i]<=75:
		c+=1
	if vet[i]>=76 and vet[i]<=100:
		d+=1

print()
print('='*50)
print(f'Intervalo[0-25] = {a}\nIntervalo [26-50] = {b}\nIntervaldo [51-75 = {c}\nIntervalo [76-100] = {c}')


