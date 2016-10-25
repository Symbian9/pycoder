import os
def test1(*args):
  print args
def test2(**args):
  print args
test1(1,2,3)
test2(a=4,b=5,c=6)

#第一个 *args 表示参数是可变的，python会把参数作为一个列表。第二个 **arg 也表示参数是可变的，python会把参数当作一个字典，因为是字典，所以参数传递必须是 a=xx, b=xx这种方式