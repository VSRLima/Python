escolha = 0
n1 = int(input('Digite o 1ª número: '))
n2 = int(input('Digite o 2ª número: '))
while escolha != 5:
    escolha = int(input('[1] somar \n'
                        '[2] multiplicar \n'
                        '[3] maior \n'
                        '[4] novos números \n'
                        '[5] sair do programa \n'
                        'Digite: '))
    if escolha == 1:
        s = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, s))
        print('=' * 20)
    elif escolha == 2:
        m = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, m))
        print('=' * 20)
    elif escolha == 3:
        if n1 > n2:
            print('{} > {}'.format(n1, n2))
        else:
            print('{} > {}'.format(n2, n1))
    elif escolha == 4:
        print('Informe os números novamente: ')
        n1 = int(input('1ª valor: '))
        n2 = int(input('2ª valor: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=' * 20)



