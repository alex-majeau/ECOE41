from math import pow

mem = [[-1]*100]*100

def solve(soma, dados):
    global mem
    global d
    global s

    if (dados == d):
        return soma == s
    
    if (soma >= s):
        return 0
    
    if (mem[soma][dados] != -1):
        return mem[soma][dados]
    
    ans = 0
    for i in range(1,7,1):
        ans += solve(soma+i,dados+1)
    
    mem[soma][dados] = ans
    return mem[soma][dados]


cases = int(input())
    
for i in range(cases):
    values = input().split()
    s = int(values[0])
    d = int(values[1])

    print("%.15f" % (solve(0,0)/(6**d)))
	

