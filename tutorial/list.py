test = [11.0, "Alice has a cat", 12, 4, "5"]


print("len(test) = " + str(len(test)))
print("test[1] = " + str(test[1]))
print("test[3:6] = " + str(test[3:6]))
print("test[1:6:2] = " + str(test[1:6:2]))
print("test[:6] = " + str(test[:6]))
print("test[-2] = " + str(test[-2]))


test.append(121)

test2 = test + [1, 2, 3]

print("len(test2) = " + str(len(test2)))

test2[0] = "Lodz"
test2[6] = 77
print(test2)
