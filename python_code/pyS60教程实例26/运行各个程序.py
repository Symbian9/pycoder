#e32.start_exe("##","")（##表示exe文件路径）,后面那个引号中加操作，如启动自带浏览器时加网址可自动打开网址


import appuifw,applist,e32
def cn(x):return x.decode("utf8")
def exit():
    if appuifw.query(cn("真的要退出吗？"),"query"):
        appuifw.app.set_exit()
list1=[]
list2=[]
list3=[]
i=0
applist=applist.applist()#其中，M是一个列表，列表中的每一项是一个元组，对应一个exe文件，元组的第一项是程序编号，第二项是程序名称，第三项是exe文件的路径。我们把这个函数与

while i<len(applist):
    list1.append(applist[i][1])#在列表中添项，见下节
    list2.append(applist[i][0])
    list3.append(applist[i][2])
    i+=1
def press():
    index=listbox.current()
    list=[cn("查看编号"),cn("查看路径"),cn("启动程序")]
    index1=appuifw.popup_menu(list,cn("查看信息"))
    if index1==0:
        appuifw.note(cn(str(list2[index])),"info")
    if index1==1:
        appuifw.note(cn(str(list3[index])),"info")
    if index1==2:
        try:
            e32.start_exe(list3[index],"")
        except:
            appuifw.note(cn("无法启动！"),"error")

    e32.Ao_lock().wait()
def about():
    appuifw.note(cn("制作：tengge\n\nQQ:930372551"),"info")
appuifw.app.menu=[(cn("关于"),about),(cn("退出"),exit)]
appuifw.app.exit_key_handler=exit
appuifw.app.body=listbox=appuifw.Listbox(list1,press)


e32.Ao_lock().wait()