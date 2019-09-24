''' Fibonacci between 0 to 50'''

first = 1
sec = 1

for i in range(51):
    if (i==0):
        print("{}: 1".format(i))
    elif(i==1):
        print("{}: 1".format(i))
    else:
        print("{}: {}".format(i, (i-1) + (i-2)))