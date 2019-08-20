string = input()

let = 0
num = 0

for i in string:
    if (i.isalpha()):
        let += 1
    else:
        num += 1

print("Let: {} \nNum:{}".format(let, num))