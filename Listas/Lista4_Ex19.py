print('Qual o melhor Sistema Operacional para uso em servidores?')
print('''\nAs possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro\n''')

opcoes=['Windows Server ',\
		'Unix           ',\
		'Linux          ',\
		'Netware        ',\
		'Mac OS         ',\
		'Outro          ']
sist=[0]*6
while True:
    while True:
        op=int(input('Digite a opção: '))
        if op>6 or op<0:
            print('Opção inválida.')
        else:
            break
    if op==0:
        break
    sist[op-1]+=1


print('\nSistema Operacional     Votos  %')
print('='*50)
cont=0
melhor=0
melhorSis=''
perc=0
for i in sist:
    print('%s   %d   %.0f%%' % (opcoes[cont], i,(i*100) / sum(sist) ))
    if i>melhor:
        melhor=i
        melhorSis=opcoes[cont]
        perc=(i*100)/sum(sist)
    cont+=1

print('='*50)
print('Total       %d' % sum(sist))
print('\nO Sistema Operacional mais votado foi o %s, com %d votos, correspondendo a %.0f%% dos votos.' % (melhorSis, melhor, perc))
