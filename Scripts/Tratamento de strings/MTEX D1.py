nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letas minúsculas é {}'.format(nome.lower()))
print('A quantidade de letras em seu nome é {}'.format(len(nome) - nome.count(' ')))
print('A quantidade de letras em seu primeiro nome é {}'.format(len(nome.split()[0])))