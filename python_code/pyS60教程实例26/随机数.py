import random,appuifw
def cn(x):return x.decode("utf8")

list=[cn("我爱"),cn("我不爱")]
a=random.choice(list)#从列表中随机取出一项
b=random.randint(1,10)#随机产生一个零到十之间的整数
appuifw.note(a+unicode(b))
