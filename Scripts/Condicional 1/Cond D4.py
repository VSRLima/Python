print('Viagens de ônibus CVC')
print('=' * 20)
nome = str(input('Qual o seu nome? '))
dis = int(input('Quantos Km vc quer viajar? '))
if dis <= 200:
    totmenor = dis * 0.5
    print('{}, você irá pagar R${:.2f} por essa viagem'.format(nome, totmenor))
else:
    totmaior = dis * 0.45
    print('{} você irá pagar R${:.2f} por essa viagem'.format(nome, totmaior))
