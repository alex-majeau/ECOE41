values = input()
values = values.split()

pi = 3.14159

A = float(values[0])
B = float(values[1])
C = float(values[2])

print("TRIANGULO: {:.3f}".format(A*C/2))
print("CIRCULO: {:.3f}".format(pi*C**2))
print("TRAPEZIO: {:.3f}".format((A+B)*C*0.5))
print("QUADRADO: {:.3f}".format(B**2))
print("RETANGULO: {:.3f}".format(A*B))