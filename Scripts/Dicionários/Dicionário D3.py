from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
dados['Idade'] = date.today().year - ano
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
print('~' * 30)
if dados['CTPS'] != 0:
    contrato = int(input('Ano de contratação: '))
    contribuição = contrato - ano
    dados['Contratação'] = contrato
    dados['Aposentadoria'] = contribuição + 35
    dados['Salário'] = int(input('Salário: '))
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
