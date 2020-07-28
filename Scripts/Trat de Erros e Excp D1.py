def leiaint(msg):
    while True:
        ok = False
        try:
            resp = int(input(msg))
            ok = True
        except ValueError:
            print('ERRO! O valor digitado não é inteiro')
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            break
        else:
            return resp
        if ok:
            break


def leiafloat(msg):
    while True:
        ok = False
        try:
            resp = float(input(msg))
            ok = True
        except ValueError:
            print('ERRO! O valor digitado não é real')
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            break
        else:
            return resp
        if ok:
            break


n = leiaint('Digite um número inteiro: ')
n1 = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar o número {n} e {n1}')
