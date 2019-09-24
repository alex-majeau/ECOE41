from math import factorial

while True:
    n = input()
    if n is '0':
        break
    else:
        separate_number = []
        answer = 0
        for i in range(len(n)):
            separate_number.append(int(n[i]))
        
        for i in range(1,len(separate_number)+1):
            aux = separate_number[i-1]*factorial(len(separate_number)-i+1)
            answer += aux
        print(answer)

