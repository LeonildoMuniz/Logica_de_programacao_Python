reajuste1=20
reajuste2=15
reajuste3=10
reajuste4=5

salarioAtual= float(input('Digite o salario atual: '))

print()
print("="*50)
print()

if salarioAtual<=280:
	aumento = salarioAtual*(reajuste1/100)
	salarioNovo=salarioAtual+aumento
	print(f'Salario atual: R$ {salarioAtual: .2f}')
	print(f'Percentual de aumento {reajuste1:.2f}%')
	print(f'Valor do reajuste: R$ {aumento: .2f}')
	print(f'Novo salario reajustado: R$ {salarioNovo: .2f}')

if salarioAtual>280 and salarioAtual<=700:
	aumento = salarioAtual*(reajuste2/100)
	salarioNovo=salarioAtual+aumento
	print(f'Salario atual: R$ {salarioAtual: .2f}')
	print(f'Percentual de aumento {reajuste2:.2f}%')
	print(f'Valor do reajuste: R$ {aumento: .2f}')
	print(f'Novo salario reajustado: R$ {salarioNovo: .2f}')

if salarioAtual>700 and salarioAtual<=1500:
	aumento = salarioAtual*(reajuste3/100)
	salarioNovo=salarioAtual+aumento
	print(f'Salario atual: R$ {salarioAtual: .2f}')
	print(f'Percentual de aumento {reajuste3:.2f}%')
	print(f'Valor do reajuste: R$ {aumento: .2f}')
	print(f'Novo salario reajustado: R$ {salarioNovo: .2f}')

if salarioAtual>1500:
	aumento = salarioAtual*(reajuste4/100)
	salarioNovo=salarioAtual+aumento
	print(f'Salario atual: R$ {salarioAtual: .2f}')
	print(f'Percentual de aumento {reajuste4:.2f}%')
	print(f'Valor do reajuste: R$ {aumento: .2f}')
	print(f'Novo salario reajustado: R$ {salarioNovo: .2f}')
