val = input()
val = val.split()

val[0] = float(val[0])
val[1] = float(val[1])
val[2] = float(val[2])

val.sort()

A = float(val[2])
B = float(val[1])
C = float(val[0])

if (A >= (B+C)):
    print("NAO FORMA TRIANGULO")
else:
    if (A**2 == (B**2 + C**2)):
        print("TRIANGULO RETANGULO")

    if (A**2 > (B**2 + C**2)):
        print("TRIANGULO OBTUSANGULO")

    if (A**2 < (B**2 + C**2)):
        print("TRIANGULO ACUTANGULO")

    if (A == B and B == C):
        print("TRIANGULO EQUILATERO")

    if ((A == B and A != C) or (A == C and A != B) or (B == C and B !=A)):
        print("TRIANGULO ISOSCELES")    
