n = int(input())
for i in range(n):
    aux = []
    sum = 0
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') # each index is the value of the letter
    L = int(input())
    aux = [input() for i in range(L)] # make a list with all entries (Bits of Python!)

    for j in range(len(aux)):  # run all words | j = element
        for k in range(len(aux[j])): # get the size of each string | k = position
            sum += j + k + letters.index(aux[j][k]) # element + position + value of letter
    print (sum)