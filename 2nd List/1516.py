while True:
    n, m = input().split()
    if (n == m == '0'):
        break
    
    lines = []
    for i in range(int(n)):
        lines.append(input())
    
    a,b = input().split()
    a2 = int(int(a)/int(n))
    b2 = int(int(b)/int(m))

    new = []
    for line in lines:
        aux = ''
        for symbol in line:
            aux += b2*symbol

        for i in range(int(a2)):
            new.append(aux)

    for newline in new:
        print(newline)
    print()