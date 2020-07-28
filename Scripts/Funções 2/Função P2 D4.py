def leiaint(msg):
    ok = False
    v = 0
    while True:
        a = str(input(msg))
        if a.isnumeric():
            v = int(a)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um valor númerico.\033[m')
        if ok:
            break
    return a


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
