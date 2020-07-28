def voto(ano):
    """
    =>Tem a função de calcular a idade e analisa-lá para saber se o indivíduo pode votar ou não.
    :param ano: Ano de nascimento do indivíduo. (int)
    """
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')


nascimento = int(input('Digite seu ano de nascimento: '))
voto(nascimento)
