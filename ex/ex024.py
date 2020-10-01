""" DESAFIO 24 - Crie um programa que leia o nome de uma cidade e diga se ela começa
    ou nao com o nome "SANTO".

"""

cidade = input('Digite um nome de cidade:')
print('SANTO' in cidade.upper())

# Correção

cid = str(input('Digite um nome de cidade:')).strip()
print(cid[:5].upper() == 'SANTO')

