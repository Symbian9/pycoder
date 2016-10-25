def add(n):
  return n%2
def mod(n):
  return n*2
lists = [3,4,5,6,7]
print map(mod,lists)
print filter(add,lists)


#map,针对列表中每项,进行操作
#filter,过滤作用,当调用函数返回"真"时,才把传入的参数返回,他不关心被调函数的返回值的大小类型,只关心他是不是真假引用