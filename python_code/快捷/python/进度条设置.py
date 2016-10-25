import dialog,e32#dialog是进度条模块
def cn(x):return x.decode("utf8")
wait=dialog.Wait(cn("请稍后…"))#设置初现字幕
wait.show()#显示进度条
e32.ao_sleep(2)#这里放上程序
wait.set_label(cn("正在安装…"))#更改显示的字幕
e32.ao_sleep(2)#这里放上程序
wait.close()#关闭进度条
