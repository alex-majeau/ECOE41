from math import factorial

while True:
    try:
        M, N = input().split()
        print(factorial(int(M))+factorial(int(N)))

    except EOFError:
        break
