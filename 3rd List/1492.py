import time

def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 

while True:
    try:
        A, B = input().split()
        counter = 0
        for i in range(int(A), int(B)+1):
            counter += countSetBits(i)
        print(counter)
    except EOFError:
        break