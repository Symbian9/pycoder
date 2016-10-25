import appuifw

def cn(x):return x.decode("utf-8")

appuifw.note(cn("你好"),"conf")

def wb():
  if appuifw.query(cn("转入文本界面？"),"query"):
    appuifw.app.body=appuifw.Text()
    appuifw.app.menu=[(cn("美女"),mv),(cn("小姐"),xj),(cn("返回"),main)]
    appuifw.app.exit_key_handler=main

def mv():
  appuifw.app.body.color=(0,0,255)
  appuifw.app.body.add(cn('美女'))
def xj():
  appuifw.app.body.color=(255,0,0)
  appuifw.app.body.add(cn('小姐'))

def exit():
  if appuifw.query(cn("确定退出吗？"),"query"):
    appuifw.app.set_exit()

def main():
  def press():
    index=listbox.current()
    appuifw.note(cn("老婆我爱你")+list[index],"info")

  list=[cn("呀"),cn("不是吗")]
  appuifw.app.body=listbox=appuifw.Listbox(list,press)
  appuifw.app.menu=[(cn("文本界面"),wb)]
  appuifw.app.exit_key_handler=exit
  
main()#执行主函数

##下面一段可避免ped一闪而过
if appuifw.app.full_name().split('\\')[-1][:-4].lower() in [u'ped', u'python', u'appmgr']:
  import e32
  app_lock = appuifw.e32.Ao_lock()
  exit = app_lock.signal
  app_lock.wait()
else: exit = appuifw.app.set_exit
##结束