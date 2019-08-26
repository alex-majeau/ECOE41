n = int(input())

for i in range(n):
    A,B = input().split()
    k = 0
    answer = []
    
    for j in range(min(len(A), len(B))):
        answer.append(A[k])
        answer.append(B[k])
        k+=1
    answer.append(A[k:])
    answer.append(B[k:])
    
    print(''.join(answer))