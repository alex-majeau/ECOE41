n = int(input())

for i in range(n):
    string = input().split()
    A = string[0]
    B = string[1]
    
    if (A[(len(A)-len(B)):] == B[:]):
        print("encaixa")
    else:
        print("nao encaixa")
