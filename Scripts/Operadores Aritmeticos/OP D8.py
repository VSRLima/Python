p = float(input('Qual o preço do produto? '))
p5= p - (p*5)/100
print('O produto com o valor R${}, vai sair por R${:.2f}, porque recebeu 5% de desconto'.format(p, p5))
