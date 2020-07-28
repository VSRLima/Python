from time import sleep
def maior(* núm):
    high = a = 0
    for v in núm:
        if v > high:
            high = v
    print(f'Os valores digitados foram:', end='')
    for c in núm:
        print(f'{c} ', end='', flush=True)
        sleep(0.3)
        a += 1
    print(f'; O valor maior é {high} e foram digitados {a} números')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
