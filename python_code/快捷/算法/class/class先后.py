class a:
  def __del__(self):
    import appuifw
    def cn(x):return x.decode('utf-8')
    appuifw.note(cn("我总是替别人擦屁股"))
  def say(self):
    import appuifw
    def cn(x):return x.decode('u8')
    appuifw.note(cn("我是路过的打酱油…"))
  def __init__(self):
    import appuifw
    def cn(x):return x.decode('u8')
    appuifw.note(cn("你猜我在代码的什么位置？"))
a().say()