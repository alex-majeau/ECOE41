from math import sqrt

val = input()
val = val.split()

A = float(val[0])
B = float(val[1])
C = float(val[2])
D = B**2-4*A*C

if(D<0 or A==0):
    print("Impossivel calcular")
else:
    print("R1 = {:.5f}".format((-B+sqrt(D))/(2*A)))
    print("R2 = {:.5f}".format((-B-sqrt(D))/(2*A)))