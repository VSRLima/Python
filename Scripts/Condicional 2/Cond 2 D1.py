print('\033[35m-=' * 11)
print('\033[1;34mPROGRAMA CASA PRÓPRIA\033[m')
print('\033[35m-=\033[m' * 11)
nome = str(input('Bom dia, qual é o seu nome? '))
salário = float(input('Qual é o seu salário? '))
casa = float(input('Qual o valor da casa? '))
anos = int(input('Em quantos anos você vai pagar? '))
meses = anos * 12
prestação = casa / meses
if prestação > (salário * 30) /100:
    print('O valor da prestação é R${:.2f}'.format(prestação))
    print('E com a regra de que a prestação não pode exceder 30% do seu salário, seu empréstimo foi:')
    print('\033[1;31mEMPRESTIMO NEGADO')
else:
    print('O valor da prestação é R${:.2f}'.format(prestação))
    print('\033[1;32mPARABÉNS!!! SEU EMPRESTIMO FOI APROVADO')