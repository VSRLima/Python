times = ('Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Ceará',
         'Corinthias', 'Corinthians', 'Coritiba', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio',
         'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Sport', 'Vasco')
print('Os 5 primeiros são:', end=' ')
for c in range(0, 6):
    print(times[c], end=' -> ')
print('Fim')
print('~' * 100)
print('Os 4 últimos são:', end=' ')
for i in range(17, 21):
    print(times[i], end=' -> ')
print('Fim')
print('~' * 100)
print(f'A tabela em ordem alfabética: {sorted(times)}')
print('~' * 100)
print(f'O Bahia está na {times.index("Bahia")+ 1}ª posição')
