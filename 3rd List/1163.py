from math import sqrt, cos, sin

def bascara (a, b, c):
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-1*b + sqrt(D))/(2*a)
        x2 = (-1*b - sqrt(D))/(2*a)

    if (x1 > 0):
        return x1
    elif (x2 > 0):
        return x2

while True:
    try:
        h = float(input())
        p1, p2 = input().split()
        n = int(input())

        G = 9.80665
        pi = 3.14159
        for i in range(n):
            alfa, vel = input().split()

            Vx = float(vel)*cos(float(alfa)*float(pi/180.0))
            Vy = float(vel)*sin(float(alfa)*float(pi/180.0))

            t = bascara((-1*G/2), Vy, h)
            d = Vx*t
            
            if (int(p1) <= d and d <= int(p2)):
                print("%.5f -> DUCK" %d)
            else:
                print("%.5f -> NUCK" %d)

    except EOFError:
        break
