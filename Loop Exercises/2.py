''' Count even and odd from a given series'''

series = input().split()

odd = 0
even = 0

for i in range(len(series)):
    if ((i%2)==0):
        even += 1
    else:
        odd += 1

print("Odd: {} \nEven: {}".format(odd, even))
    