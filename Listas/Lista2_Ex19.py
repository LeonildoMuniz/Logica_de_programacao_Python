cont1=0
cont2=0

num=int(input('Digite um valor menor que 1000: '))
num2=num


if num<=1000:
	while num>99:
		num-=100
		cont1+=1
	while num>9:
		num-=10
		cont2+=1
	
	if cont1>1 and cont2>1 and num>1:
		print(f'{num2} = {cont1} centenas, {cont2} dezenas e {num} unidades')
	if cont1==1 and cont2>1 and num>1:
		print(f'{num2} = {cont1} centena, {cont2} dezenas e {num} unidades')
	if cont1>1 and cont2==1 and num>1:
		print(f'{num2} = {cont1} centenas, {cont2} dezena e {num} unidades')
	if cont1>1 and cont2>1 and num==1:
		print(f'{num2} = {cont1} centenas, {cont2} dezenas e {num} unidade')
	if cont1==1 and cont2==1 and num==1:
		print(f'{num2} = {cont1} centena, {cont2} dezena e {num} unidade')
	if cont1>1 and cont2==1 and num==1:
		print(f'{num2} = {cont1} centenas, {cont2} dezena e {num} unidade')	
	if cont1==1 and cont2>1 and num==1:
		print(f'{num2} = {cont1} centena, {cont2} dezenas e {num} unidade')
	if cont1==1 and cont2==1 and num>1:
		print(f'{num2} = {cont1} centena, {cont2} dezena e {num} unidades')	
	if cont1>1 and cont2>1 and num==0:
		print(f'{num2} = {cont1} centenas, {cont2} dezenas')			
	if cont1==1 and cont2==1 and num==0:
		print(f'{num2} = {cont1} centena, {cont2} dezena')		
	if cont1>1 and cont2==1 and num==0:
		print(f'{num2} = {cont1} centenas, {cont2} dezena')	
	if cont1==1 and cont2>1 and num==0:
		print(f'{num2} = {cont1} centena, {cont2} dezenas')	
	if cont1>1 and cont2==0 and num>1:
		print(f'{num2} = {cont1} centenas, {num} unidades')	
	if cont1==1 and cont2==0 and num>1:
		print(f'{num2} = {cont1} centena, {num} unidades')	
	if cont1==1 and cont2==0 and num==1:
		print(f'{num2} = {cont1} centena, {num} unidade')
	if cont1>1 and cont2==0 and num==1:
		print(f'{num2} = {cont1} centenas, {num} unidade')				
	if cont1==1 and cont2==0 and num>1:
		print(f'{num2} = {cont1} centena, {num} unidades')		
	if cont1==0 and cont2>1 and num>1:
		print(f'{num2} = {cont2} dezenas e {num} unidades')
	if cont1==0 and cont2==1 and num>1:
		print(f'{num2} = {cont2} dezena e {num} unidades')
	if cont1==0 and cont2>1 and num==1:
		print(f'{num2} = {cont2} dezenas e {num} unidade')		
	if cont1==0 and cont2==1 and num==1:
		print(f'{num2} = {cont2} dezena e {num} unidade')
	if cont1>1 and cont2==0 and num==0:
		print(f'{num2} = {cont1} centenas')
	if cont1==1 and cont2==0 and num==0:
		print(f'{num2} = {cont1} centena')
	if cont1==0 and cont2>1 and num==0:
		print(f'{num2} = {cont2} dezenas')
	if cont1==0 and cont2==1 and num==0:
		print(f'{num2} = {cont2} dezena')
	if cont1==0 and cont2==0 and num>1:
		print(f'{num2} = {num} unidades')
	if cont1==0 and cont2==0 and num==1:
		print(f'{num2} = {num} unidade')

else:
	print('Numero digitado maior que 1000')
