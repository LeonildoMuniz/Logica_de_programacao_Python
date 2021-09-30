cont=0
print('Responda as pertuntas abaixo como Sim ou Não')

p1=input("Telefonou para a vítima?: ")
if p1=="Sim":
	cont+=1
p2=input("Esteve no local do crime?: ")
if p2=="Sim":
	cont+=1
p3=input("Mora perto da vítima?: ")
if p3=="Sim":
	cont+=1
p4=input("Devia para a vítima?: ")
if p4=="Sim":
	cont+=1
p5=input("Já trabalhou com a vítima?: ")
if p5=="Sim":
	cont+=1

print()
print('='*50)
print()

if cont==2:
	print('Suspeita')
if cont>=3 and cont<=4:
	print('Cúmplice')
if cont==5:
	print('Assassino')
if cont<2:
	print('Inocente')
