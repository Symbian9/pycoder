import appuifw,e32
def plus(a,b):
    c=a+b
    return c
result=plus(20,30)
appuifw.app.body.set(unicode(result))#要将数值格式的转换为unicode格式的才能正常显示！
e32.Ao_lock().wait()
