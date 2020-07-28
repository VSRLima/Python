frase = str(input('Digite uma frase: ')).strip().upper()
print('Quantas vezes aparece a letra "A"? {}'.format(frase.count('A')))
print('Em que posição a letra "A" aparece primeiro? {}'.format(frase.find('A')))
print('Em que posição a letra "A" aparece pela última vez? {}'.format((frase.rfind('A'))))
