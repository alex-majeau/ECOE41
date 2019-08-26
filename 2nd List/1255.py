n = int(input())

for i in range(n):
        string = input().lower()
        values = {}
        for letter in string:
                if (letter in values and letter.isalpha()):
                        values[letter] += 1
                elif (letter.isalpha()):
                        values[letter] = 1
                else:
                        continue
        bigger = 0
        for i in sorted(values, key=values.get):
                if (values[i]>bigger):
                        bigger = values[i]                
        new = ''
        for i in sorted(values, key=values.get):
                if (values[i]==bigger):
                        new += i
        print(''.join(sorted(new)))