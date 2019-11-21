import math as m


def power(a, b):
    i = 1
    res = a

    while i < b:
        res *= a
        i += 1

    return res


def max(l):
    max = -99999999
    i = 0
    while i < 10:
        a = int(input())
        if(max < a):
            max = a
        i += 1
    return max


def info_list(l):
    return max(l)


def quadraticEQ(a, b, c):
    d = m.sqrt(b**2 - 4 * a * c)
    x1 = (a-d)/(2*a)
    x2 = (a+d)/(2*a)

    print("x1 = " + str(x1))
    print("x2 = " + str(x2))
