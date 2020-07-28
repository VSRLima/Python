nome = input('Qual o nome do funcionário? ')
sal = float(input('Qual o salário de {} ? R$'.format(nome)))
sal15 = sal + (sal*15 / 100)
print('O funcionário {} recebe R${} e o seu salário vai sofrer um acréscimo de 15%, que resulta em R${}'.format(nome, sal, sal15))
