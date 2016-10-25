import appuifw2,appuifw

appuifw2.app.body=m=appuifw2.Text(skinned=1)
def cn(x):return x.decode("utf-8")
m.focus = False
m.font = (u'Sans MT 936_s60', 16)
m.color = (0)
m.set(cn('很抱歉，未找到相关的方程式，您可以尝试交换物质AB的顺序'))


appuifw.e32.Ao_lock().wait()