#python可以象c++一样有运算符重载吗
#我想重新定义+,让两个对象相加,C++里有运算符重载,python里呢?

class A:
  def __init__(self, v = 0):
    self.a = v
  def __add__(self, other):
    return A(self.a + other.a)
  def __str__(self):
    return str(self.a)
a = A(2)
print 'a:', a
b = A(10)
print 'b:', b
c = a + b
print 'c:', c

#重新定义类的__add__方法,就相当于C++里的运算符重载 + 了
# - 是  __sub__
# * 是  __mul__
# /  是  __div__