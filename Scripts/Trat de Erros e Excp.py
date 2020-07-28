pessoas = dict()
pessoas['Nomes'] = 'Ana Paula Vieira', 'Cláudio Mendonça', 'Gustavo Guanabara'


def cadastro(n):
    print('~' * 30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('~' * 30)
    print('1- Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do Sistema')
    print('~' * 30)
    resposta = int(input(n))
    if n == 1:
        print(pessoas)
    return resposta


resp = cadastro('Sua opção: ')