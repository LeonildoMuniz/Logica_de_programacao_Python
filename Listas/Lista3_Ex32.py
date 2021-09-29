fat=1;
vet=[]
vet2=[]


num=int(input('Fatorial de: '))
num2=num
for i in range(num):
	fat=fat+(fat*i)

for i in range(num,0,-1):
	vet.append(i)

	
print(f'{num}! = {vet} = {fat} ')
