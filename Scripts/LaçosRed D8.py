from datetime import date
s = 0
smais = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    if date.today().year - ano <= 21:
        s += 1
    else:
        smais += 1
print('A quantidade de pessoas que não atingiram a maior idade foram {} pessoas.'.format(s))
print('A quantidade de pessoas que atingiram a maior idade foram {} pessoas.'.format(smais))
