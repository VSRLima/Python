from random import choice
print('Colégio Santa Clara')
print('='*25)
name1 = input('Digite o nome do 1° aluno: ')
name2 = input('Digite o nome do 2° aluno: ')
name3 = input('Digite o nome do 3° aluno: ')
name4 = input('Digite o nome do 4° aluno: ')
seq = [name1, name2, name3, name4]
choice(seq)
print('O aluno sorteado para limpar o quadro foi {}.'.format(choice(seq)))
