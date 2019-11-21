print("Hello World!\n")
# this is my first python script (!not)

b = 11.0
B = "Alice has a cat"
var1 = 12
var2 = 4
Var3 = "5"

print("b is " + type(b).__name__)
print("B is " + type(B).__name__)
print("var1 is " + type(var1).__name__)
print("var2 is " + type(var2).__name__)
print("Var3 is " + type(Var3).__name__)

print("\n")

print("var1 + var2 = " + str(var1+var2))
print("B + \" i psa\" = " + B + " i psa")
print("b % var2 = " + str(b % var2))
print("b * var1 = " + str(b * var1))
print("b ** var1 = " + str(b ** var1))
print("B * var1 = " + B * var1)
try:
    print("B * Var3 = " + B * Var3)
except TypeError as te:
    print("B * Var3 = ERROR: " + str(te))

print("\n")

print("len(B)=" + str(len(B)))

print("B[0] = " + str(B[0]))
print("B[1] = " + str(B[1]))
print("B[3:6] = " + str(B[3:6]))
print("B[3:] = " + str(B[3:]))
print("B[:6] = " + str(B[:6]))
print("B[-2] = " + str(B[-2]))


print("\n")

print("B*int(Var3) = " + str(B*int(Var3)))
print("type(str(3)) = " + str(type(str(3))))

c = B[:10] + str(3) + B[-4:] + "s"
print(c)
d = c[:-4] + "dogs"
print(d)