#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-03-11 14:48:32
# @Last Modified by:   anchen
# @Last Modified time: 2016-03-11 16:05:11


from math import sqrt


# if __name__ == '__main__':
#     N = 100
#     a = list(range(0, N))
#     for i in range(2, int(sqrt(N))):
#         for j in range(i + 1, N):
#             if a[i] != 0 and a[j] != 0:
#                 if a[j] % a[i] == 0:
#                     a[j] = 0

#     for i in range(2, N):
#         if a[i] != 0:
#             print('%5d' % a[i])
#             if (i - 2) % 10 == 0:
#                 print()



# a = (1, 2, 3, 4)

# for b1 in a:
#     for b2 in a:
#         for b3 in a:
#             if b1 != b2 and b2 != b3 and b1 != b3:
#                 print('%d%d%d' % (b1, b2, b3))


# s = ' '

# for i in range(1, 10):
#     for j in range(1, 10):
#         print('%d * %d = %-3d' % (i, j, i * j))



print('please input two numbers')

num1, num2 = int(input()), int(input())

if num1 > num2:
    num1 ^= num2
    num2 ^= num1
    num1 ^= num1
a, b = num1, num2

while b != 0:
    a %= b
    a ^= b
    b ^= a
    a ^= b
print('common divisor: %d' % a)
print('common multiple: %d' % (num1 * num2 / a))
