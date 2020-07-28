nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no \033[32mBr\033[33mas\033[34mil\033[m.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('\033[31mBelo nome feminino\033[m')
else:
    print('Seu nome é bem normal.')
print('\033[4;36mTenha um bom dia {}'.format(nome))