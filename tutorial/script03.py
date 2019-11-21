import math

print("Insert a: ")
a = float(input())
print("Insert b: ")
b = float(input())
print("Insert c: ")
c = float(input())

d = math.sqrt(b**2 - 4 * a * c)
x1 = (a-d)/(2*a)
x2 = (a+d)/(2*a)

print("x1 = " + str(x1))
print("x2 = " + str(x2))
