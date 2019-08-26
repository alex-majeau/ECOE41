n = int(input())

for i in range(n):
    A = input()
    answer = []*len(A)
    answer.append(A[int(len(A)/2)-1::-1])
    answer.append(A[:int(len(A)/2)-1:-1])   
    print(''.join(answer))