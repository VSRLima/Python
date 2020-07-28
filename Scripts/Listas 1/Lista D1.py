valores = list()
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input('Digite um número: ')))
    if c == 0 or maior < valores[c]:
        maior = valores[c]
    if c == 0 or menor > valores[c]:
        menor = valores[c]
print(f'A lista é {valores}')
print(f'O menor número da lista é {menor} e suas posições na lista são ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()
print(f'O maior número da lista é {maior} e suas posições na lista são ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
