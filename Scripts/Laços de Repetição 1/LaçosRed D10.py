anos = 0
maior = 0
nome2 = ''
totm = 0
for c in range(1, 5):
    print('-----{}ª pessoa-----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    anos += idade
    if c == 1 and sexo == 'M':
        maior = idade
        nome2 = nome
    if sexo == 'M' and idade > maior:
        maior = idade
        nome2 = nome
    if sexo == 'F' and idade < 20:
        totm += 1
print('A média de idade do grupo é {} anos'.format(anos / 4))
print('O homem mais velho é {} e sua idade é {} anos'.format(nome2, maior))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totm))
