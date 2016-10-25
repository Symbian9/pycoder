import appuifw
def cn(x):return x.decode("utf-8")
#异常捕获，若不执行测试的内容就会捕获到异常
try:
    a,b=appuifw.multi_query(cn("乐讯昵称"), cn("乐讯ID"))
    appuifw.note(a+"\n"+b, "info")

except: 
   appuifw.note(cn("你选择了否"), "info")
