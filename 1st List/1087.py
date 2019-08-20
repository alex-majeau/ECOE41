'''
Queen moviments:
- SAME PLACE: when x1 == x2 and y1 == y2        --> 0
- ROW: when y1 == y2                            --> 1
- COLUMN: when x1 == x2                         --> 1
- DIAGONAL: 
            1)distance in x == distance in y    --> 1
            2)distance in x != distance in y    --> 2

Stop requirement: all of the inputs are 0
'''
while True:
    values = input().split()

    x1 = int(values[0])
    y1 = int(values[1])
    x2 = int(values[2])
    y2 = int(values[3])

    # Stop requirement
    if(x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0):
        break
    
    elif (x1==x2 and y1 == y2):
        print("0")

    elif(x1 == x2 or y1 == y2):
        print("1") 
    
    elif(abs(x2-x1) == abs(y2-y1)):
        print("1")
    
    else:
        print("2")
    
    