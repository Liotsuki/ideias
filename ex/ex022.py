''' DESAFIO 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
 O nome com todas as letras maiusculas
 O nome com todas minusculas
 Quantas letras ao todo (sem considerar espaços)
 Quantas letras tem o primeiro nome. '''

nome = str(input('Digite o nome completo:'))
n = nome.split()
m = nome.replace(" ","")
print('Vc digitou o nome {}'.format(nome))
print('Em maiuscula é {}'.format(nome.upper()))
print('Em miniscula é {}'.format(nome.lower()))
print('O total de letra é:{}'.format(len(m)))
print('o primeiro nome é {} e tem {} letras'.format(n[0], len(n[0])))

# correção

nome = str(input('Digite o nome:')).strip()
print('Vc digitou o nome {}'.format(nome))
print('Em maiuscula é {}'.format(nome.upper()))
print('Em miniscula é {}'.format(nome.lower()))
print('Seu nome tem {} de letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))


