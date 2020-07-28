print('=' * 12)
print('{:=^12}'.format('LOJAS REIS'))
print('=' * 12)
produto = float(input('Qual o valor do produto? R$'))
fpay = int(input('FORMAS DE PAGAMENTO\n'
                 '[1] à vista dinheiro/cheque\n'
                 '[2] à vista cartão\n'
                 '[3] 2x no cartão\n'
                 '[4] 3x ou mais no cartão\n'
                 'Qual é a opção? '))
if fpay == 1:
    avis = produto - ((produto * 10) / 100)
    print('Com 10% de desconto o valor do produto sairá a R${:.2f}'.format(avis))
elif fpay == 2:
    avisc = produto - ((produto * 5) / 100)
    print('Com 5% de desconto o valor do produto sairá a R${:.2f}'.format(avisc))
elif fpay == 3:
    duasc = produto / 2
    print('O produto de valor R${}, vai sair por R${:.2f} 2x no cartão'.format(produto, duasc))
elif fpay == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = produto + ((produto * 20) / 100)
    parcelas2 = juros / parcelas
    print('Foi acrescentado 20% que resulta em R${:.2f}, por parcelas de {}x vai sair por R${:.2f}'.format(juros, parcelas, parcelas2))
else:
    print('OPÇÃO INVÁLIDA de pagamento. TENTE NOVAMENTE!')
print('OBRIGADO E VOLTE SEMPRE!')