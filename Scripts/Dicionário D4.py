dados = {}
lista = []
dados['Nome'] = str(input('Digite o nome do Jogador: '))
dados['Partidas'] = int(input(f'Quantas partidas o jogador {dados["Nome"]} jogou? '))
s = 0
for c in range(0, dados['Partidas']):
    lista.append(int(input(f'Quantos gols foram feitos na partida {c + 1}: ')))
    dados['gols'] = lista[:]
    s += lista[c]
dados['Total de gols'] = s
print('~' * 30)
print(dados)
print('~' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('~' * 30)
print(f'O jogador {dados["Nome"]} jogou {dados["Partidas"]} partidas.')
for c in range(0, len(lista)):
    print(f'Na partida {c + 1}, fez {lista[c]} gols')
print(f'Foi um total de {dados["Total de gols"]} gols')
