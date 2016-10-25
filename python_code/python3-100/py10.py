# import sys

# a = 1
# b = 219

# sys.stdout.write(chr(a))
# sys.stdout.write(chr(a))
# print(' ')

# for i in range(1, 11):
#     for j in range(1, i):
#         sys.stdout.write(chr(b))
#         sys.stdout.write(chr(b))
#     print(' ')
#

for i in range(1, 10):
    for j in range(1, i+1):
        result = i * j
        print('%d * %d = %-3d' % (i, j, result), end=' ')
    print()