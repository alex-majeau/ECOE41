
led_qtd =  {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}

n = int(input())

for i in range(n):
    leds = 0
    v = input()
    for num in v:
        leds+=led_qtd[num]
    print("{} leds".format(leds))
