#DESAFIO 19 - Um professor quer sortear um dos seus quatros alunos para apagar
# o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o
# nome do escolhido.


from random import choice
lista = []
for c in range(1, 5):
    aluno = input(f'Digite o nome do {c} aluno:')
    lista.append(aluno)
aluno_escolhido = choice(lista)
print('O aluno escolhido é {}'.format(aluno_escolhido))

#correção..

import random
n1 = str(input('Primeiro aluno'))
n2 = str(input('Segundo aluno'))
n3 = str(input('Terceiro aluno'))
n4 = str(input('Quarto aluno'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido é {}'.format(escolhido))