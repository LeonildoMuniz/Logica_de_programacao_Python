q1="A"
q2="B"
q3="C"
q4="D"
q5="E"
q6="E"
q7="D"
q8="C"
q9="B"
q10="A"
aluno=[]
resp=[]
result=0
cont=0


inicio=int(input('Digite 1 para iniciar: '))

while inicio==1:
	alu=input('Nome do aluno: ')
	aluno.append(alu)
	cont+=1
	print('Entre com as respostas das alternativas!')
	print('='*50)
	for i in range(10):
		alt=input(f'Resposta {i+1} questão:  ')
		if i==0 and alt==q1:
			result+=1
		if i==1 and alt==q2:
			result+=1
		if i==2 and alt==q3:
			result+=1
		if i==3 and alt==q4:
			result+=1
		if i==4 and alt==q5:
			result+=1
		if i==5 and alt==q6:
			result+=1
		if i==7 and alt==q8:
			result+=1
		if i==9 and alt==q10:
			result+=1
	resp.append(result)
	inicio=int(input('Digite 1 para novo aluno 0 para sair: '))

cont2=0
for i in range(cont):
	for j in range(cont):
		if resp[i]>=resp[j]:
			cont2+=1
	if cont2==cont:
			print('='*50)
			print(f'Maior acerto {aluno[i]} = {resp[i]}')
cont2=0
for i in range(cont):
	for j in range(cont):
		if resp[i]<=resp[j]:
			cont2+=1
	if cont2==cont:
			print('='*50)
			print(f'Menor acerto {aluno[i]} = {resp[i]}')
cont2=0

print('='*50)
print(f'Total de alunos que usaram o sistema: {cont}')
