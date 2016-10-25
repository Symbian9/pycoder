

x = int(input('input a number: '))
a = x // 10000
b = x % 10000 // 1000
c = x % 1000 // 100
d = x % 100 // 10
e = x % 10

if a != 0:
    print("there are 5 ", e, d, c, b, a)
elif b != 0:
    print("there are 4 ", d, c, b, a)
elif c != 0:
    print("there are 3 ", e, d, c)
elif d != 0:
    print("there are 2 ", e, d)
else:
    print('there are 1 ', e)
