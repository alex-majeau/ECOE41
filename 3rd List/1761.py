from math import tan

while True:
    try:
        PI = 3.141592654
        a, b, c = input().split()
        value = (float(c) + (float(b) * tan(float(a)*PI/180.0))) * 5
        print("%.2f" % value)

    except EOFError:
        break

