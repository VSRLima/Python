from random import randrange
print('Vamos jogar Par ou Ímpar')
print('~' * 20)
c = 0
while True:
    alea = randrange(11)
    escolha = 'a'
    n = int(input('Qual é o número? '))
    s = alea + n
    while not escolha in 'PI':
        escolha = str(input('Você quer Par ou Ímpar? [P/I] ')).upper().strip()[0]
    if s % 2 == 0 and escolha == 'P':
        print(f'VOCÊ GANHOU! O Pc colocou {alea} e você {n} e a soma desses dois resultou em {s} que é par')
    elif s % 2 == 0 and escolha == 'I':
        print(f'VOCÊ PERDEU! O Pc colocou {alea} e você {n} e a soma desses dois resultou em {s} que é par')
        break
    elif s % 2 == 1 and escolha == 'I':
        print(f'VOCÊ GANHOU! O Pc colocou {alea} e você {n} e a soma desses dois resultou em {s} que é ímpar')
    elif s % 2 == 1 and escolha == 'P':
        print(f'VOCÊ PERDEU! O Pc colocou {alea} e você {n} e a soma desses dois resultou em {s} que é ímpar')
        break
    c += 1
    print('~' * 20)
    print('Vamos jogar novamente...')
    print('~' * 20)
print(f'GAME OVER! Você ganhou {c}x')
