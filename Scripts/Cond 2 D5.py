print('=' * 20)
print('Colégio Santa Maria')
print('=' * 20)
print('Média do aluno')
print('=' * 20)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
if média < 5.0:
    print('\033[31mREPROVADO\033[m')
elif 5.0 <= média <= 6.9:
    print('\033[33mRECUPERAÇÃO\033[m')
else:
    print('\033[32mAPROVADO\033[m')
