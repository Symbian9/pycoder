# a = 1.0
# b = 2.0
# s = 0

# for n in range(1, 21):
#     s += b / a
#     a, b = b, a + b
# print(s)

# from functools import reduce

# l = [ ]

# for n in range(1, 21):
#     a, b = b, a + b
#     l.append(b / a)
# print(reduce(lambda x, y: x + y, l))
#
#
a,b,s=2.,1.,0.
for n in range(1,20+1):
  s+=a/b
  a=a+b
  b=a-b
print("sum is %9.6f" % s)