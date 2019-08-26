while True:
    try: 
        rw = input().lower() 
        p = int(input())

        counter = 0
        subcounter = 0
        for letter in rw:
            if (letter is 'w'):
                counter += 1
                subcounter = 0
            elif (letter is 'r'):
                if(subcounter == 0):
                    counter += 1
                if(subcounter == p):
                    subcounter = 0
                    counter += 1
                subcounter += 1
        print(counter)
    except EOFError:
        break