while True:
    n = input()
    if len(n)<3: # it's a number
        n = int(n)
        if n < 0:
            break
        else:
            print("0x"+format(n, '01X'))
    else:
        if n[1] is 'x':
            dec = int(n[2:], 16)
            print(dec)
        else:
            n = int(n)
            if n < 0:
                break
            else:
                print("0x"+format(n, '01X'))
