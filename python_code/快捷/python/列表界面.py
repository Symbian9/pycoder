import appuifw,e32
def cn(x):return x.decode('utf-8')
appuifw.app.body=appuifw.Listbox([(cn('短信息'),cn('东东测试')),(cn('10086'),cn('py列表测试'))])

e32.ao_sleep(5)