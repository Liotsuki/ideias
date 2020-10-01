""" DESAFIO 28 - Escreva um programa que faça o computador "pensar" em um numero
    inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero
    escolhido pelo computador.
    O programa devera escrever na tela se o usuario venceu ou nao.

"""
print('*' * 50)
print('Sistema descubra qual o numero')
print('*' * 50)
n = int(input('Digite um numero:'))
print('*' * 50)
print('Boa Sorte!')
print('*' * 50)
if n == 3:
    print('Voce digitou: {}'.format(n))
    print('Voce Ganhou')
else:
    print('Voce digitou: {}'.format(n))
    print('Tente outra vez')
