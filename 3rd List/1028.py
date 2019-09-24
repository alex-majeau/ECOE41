def mdc(a, b):
    resto = None
    while resto != 0:
        resto = a % b
        a = b
        b = resto
    return a


N = int(input())
for i in range(N):
    F1,F2 = input().split()
    print(mdc(int(F1), int(F2)))