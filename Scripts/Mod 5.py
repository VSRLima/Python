from random import shuffle
print('Colégio Santa Clara')
print('='*29)
name1 = input('Digite o nome do 1° aluno: ')
name2 = input('Digite o nome do 2° aluno: ')
name3 = input('Digite o nome do 3° aluno: ')
name4 = input('Digite o nome do 4° aluno: ')
seq = [name1, name2, name3, name4]
shuffle(seq)
print('A ordem de apresentação é \n {}'.format(seq))
print('=' * 29)
