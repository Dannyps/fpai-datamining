print("a: ")
a = int(input())
print("b: ")
b = int(input())

i = 1
res = a

while i < b:
    res *= a
    i += 1

print(res)
print("should equal")
print(a**b)
