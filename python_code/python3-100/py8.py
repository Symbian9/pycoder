for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print('%d * %d = %-3d' % (i, j, result), end=' ')
    print()

# i = 9
# while i < 10:
#     j = 1
#     while j < 10:
#         result = i * j
#         print('%d * %d = %-3d' % (i, j, result), end=' ')
#         j += 1
#     i -= 1
#     print()