''' Find numbers divisible by 7 and multiple of 5 between 1500 and 2700'''


for i in range(1500, 2701):
    five = False
    seven = False

    if((i%5)==0):
        five = True
    if((i%7)==0):
        seven = True
    
    if (five and seven):
        print(i)
        