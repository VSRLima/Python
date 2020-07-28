print('Calculador de IMC')
print('=' * 20)
nome = str(input('Olá! Qual seu nome? '))
altura = float(input('{}, qual a sua altura? (m) '.format(nome).capitalize()))
peso = float(input('{}, qual é o seu peso? (Kg) '.format(nome).capitalize()))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('{}, você está muito magro! Seu IMC é {:.2f}'.format(nome, imc).capitalize())
elif 18.5 < imc < 24.9:
    print('{}, você está no peso normal! Seu IMC é {:.2f}'.format(nome, imc).capitalize())
    print('PARABÉNS!')
elif 25 < imc < 29.9:
    print('{}, você está com sobrepeso! Seu IMC é {:.2f}'.format(nome, imc).capitalize())
elif 30 < imc < 39.9:
    print('{}, você está com obesidade! Seu IMC é {:.2f}'.format(nome, imc).capitalize())
else:
    print('{}, você está com obesidade grave! Seu IMC é {:.2f}'.format(nome, imc).capitalize())
