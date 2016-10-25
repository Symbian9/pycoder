from math import sqrt
from sys import stdout


count = 0
leap = 1

for m in range(101, 201):
    k = int(sqrt(m + 1))
    for i in range(2, k + 1):
        if m % i == 0:
            leap = 0
            break
        if leap == 1:
            print('%-4d' % m)
            count += 1
            if count % 10 == 0:     # 每输出10个素数，打印一个空行
                print()
            break
        leap = 1
print('The total is %d' % count)