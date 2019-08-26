n = int(input())

for i in range(n):
    string = input()
    pos = int(input())
    output = [None]*len(string)
    for j in range(len(string)):
        if(ord(string[j])-pos < 65):
            output[j] = 91-(65-(ord(string[j])-pos))
        else:
            output[j] = ord(string[j])-pos
        output[j] = chr(output[j])
    print(''.join(output))