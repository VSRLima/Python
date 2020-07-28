print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('=' * 32)
cores = {'azul':'\033[1;34;41m',
         'roxo':'\033[1;35;40m',
         'amarelo':'\033[1;33;45m',
         'vermelho':'\033[1;31;46m',
         'negative':'\033[7;30m',
         'limpa':'\033[m'}
idade = int(input('Quantos anos o atleta tem? '))
if idade <= 9:
    print('{}ATLETA MIRIM{}'.format(cores['azul'], cores['limpa']))
elif idade <= 14:
    print('{}ATLETA INFANTIL{}'.format(cores['roxo'], cores['limpa']))
elif idade <= 19:
    print('{}ATLETA JUNIOR{}'.format(cores['amarelo'], cores['limpa']))
elif idade <= 25:
    print('{}ATLETA SÊNIOR{}'.format(cores['vermelho'], cores['limpa']))
else:
    print('{}ATLETA MASTER{}'.format(cores['negative'], cores['limpa']))


