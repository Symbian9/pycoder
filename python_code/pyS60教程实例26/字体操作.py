import appuifw,e32
def cn(x):return x.decode("utf8")
appuifw.app.body= m =appuifw.Text()
m.color=(255,0,0)#红色，第一种表示方法
m.add(cn("我爱Python!\n"))
m.color=0x0000ff#蓝色，第二种表示方法
m.add(cn("教程是tengge写的。\n"))
m.style=appuifw.HIGHLIGHT_ROUNDED
m.add(cn("这是高亮圆体！\n"))
m.style=appuifw.HIGHLIGHT_SHADOW
m.add(cn("这是高亮阴影！\n"))
m.style=appuifw.HIGHLIGHT_STANDARD
m.add(cn("这是高亮标准！\n"))
m.style=appuifw.STYLE_BOLD
m.add(cn("这是粗体！\n"))
m.style=appuifw.STYLE_ITALIC
m.add(cn("这是斜体！\n"))
m.style=appuifw.STYLE_STRIKETHROUGH
m.add(cn("这是删除线！\n"))
m.style=appuifw.STYLE_UNDERLINE
m.add(cn("这是下划线！\n"))

e32.Ao_lock().wait()

