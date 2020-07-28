def área(a, b):
    ar = a * b
    print(f'A área do terreno {a:.2f}X{b:.2f} é {ar:.2f} m²')


largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Digite o comprimento do terreno (m): '))
área(largura, comprimento)
