inss=10
sindicato=3
fgts=11
ir1=0
ir2=5
ir3=10
ir4=20

horasTrabalhadas = float(input('Digite o total de horas trabalhadas: '))
valorHora = float(input('Digite o valor por hora: '))

print()
print("="*50)
print()

salarioBruto = valorHora*horasTrabalhadas
vlrInss=salarioBruto*(inss/100)
vlrSindicato=salarioBruto*(sindicato/100)
vlrFgts=salarioBruto*(fgts/100)

if salarioBruto<=900:
	vlrIr=salarioBruto*(ir1/100)
	descontos=vlrInss+vlrSindicato+vlrIr
	salarioLiquido=salarioBruto-descontos
	print(f'Salário Bruto: R$ {salarioBruto: .2f}')
	print(f'(-) IR ({ir1:.0f}%): R$ {vlrIr: .2f}')
	print(f'(-) INSS (10%): R$ {vlrInss: .2f}')
	print(f'(-) Sindicato (3%): R$ {vlrSindicato: .2f}')
	print(f'FGTS (11%): R$ {vlrFgts: .2f}')
	print(f'Total de descontos: R$ {descontos: .2f}')
	print(f'Salário Liquido: R$ {salarioLiquido: .2f}')

if salarioBruto>900 and salarioBruto<=1500:
	vlrIr=salarioBruto*(ir2/100)
	descontos=vlrInss+vlrSindicato+vlrIr
	salarioLiquido=salarioBruto-descontos
	print(f'Salário Bruto: R$ {salarioBruto: .2f}')
	print(f'(-) IR ({ir2:.0f}%): R$ {vlrIr: .2f}')
	print(f'(-) INSS (10%): R$ {vlrInss: .2f}')
	print(f'(-) Sindicato (3%): R$ {vlrSindicato: .2f}')
	print(f'FGTS (11%): R$ {vlrFgts: .2f}')
	print(f'Total de descontos: R$ {descontos: .2f}')
	print(f'Salário Liquido: R$ {salarioLiquido: .2f}')

if salarioBruto>1500 and salarioBruto<=2500:
	vlrIr=salarioBruto*(ir3/100)
	descontos=vlrInss+vlrSindicato+vlrIr
	salarioLiquido=salarioBruto-descontos
	print(f'Salário Bruto: R$ {salarioBruto: .2f}')
	print(f'(-) IR ({ir3:.0f}%): R$ {vlrIr: .2f}')
	print(f'(-) INSS (10%): R$ {vlrInss: .2f}')
	print(f'(-) Sindicato (3%): R$ {vlrSindicato: .2f}')
	print(f'FGTS (11%): R$ {vlrFgts: .2f}')
	print(f'Total de descontos: R$ {descontos: .2f}')
	print(f'Salário Liquido: R$ {salarioLiquido: .2f}')

if salarioBruto>2500:
	vlrIr=salarioBruto*(ir4/100)
	descontos=vlrInss+vlrSindicato+vlrIr
	salarioLiquido=salarioBruto-descontos
	print(f'Salário Bruto: R$ {salarioBruto: .2f}')
	print(f'(-) IR ({ir4:.0f}%): R$ {vlrIr: .2f}')
	print(f'(-) INSS (10%): R$ {vlrInss: .2f}')
	print(f'(-) Sindicato (3%): R$ {vlrSindicato: .2f}')
	print(f'FGTS (11%): R$ {vlrFgts: .2f}')
	print(f'Total de descontos: R$ {descontos: .2f}')
	print(f'Salário Liquido: R$ {salarioLiquido: .2f}')
