from math import gcd

n = int(input())
for i in range(1, n + 1):
    S1 = int(input(), 2)
    S2 = int(input(), 2)
    if (gcd(S1, S2) != 1):
        msg = "All you need is love!"
    else:
        msg = "Love is not all you need!"
        
    print("Pair #{}: {}".format(i, msg))