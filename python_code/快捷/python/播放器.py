import appuifw,e32
import audio#与音频播放的模块
import powlite_fm#一个资源管理器模块
def cn(x):return x.decode("utf-8")
appuifw.app.body=m=appuifw.Text(cn("请按选项选择歌曲"))
m.focus=False#设置焦点为无，若“True”，则有焦点，可以输入文字
def play():
    global path,p#将path和p设为全局变量，以便在其他函数中使用
    path=powlite_fm.manager().AskUser("e:\\sounds\\",ext=[".mp3",".wav",".wma"])
#调用powlite_fm中manager函数中的AskUser函数打开资源管理器，并显示mp3,wav,wma格式的文件，返回打开的路径，路径已为unicode格式
    try:
        p=audio.Sound.open(path)#打开音频文件
        p.set_volume(3)#设置音量
        p.play(2,3)#连续播放两次，之间隔三秒
        appuifw.app.menu=[(cn("暂停\播放"),pause),(cn("停止播放"),stop),(cn("音量控制"),((cn("加大"),vol_up),(cn("减小"),vol_down)))]
    except:
        appuifw.note(cn("没选择歌曲！"),"error")
def playagain():
    p.play(2,3)
    
def stop():
    p.stop()
    appuifw.app.menu=[(cn("继续播放"),playagain),(cn("重新选曲"),play)]
def vol_up():
    v=p.current_volume()#取得当前音量
    p.set_volume(v+1)
def vol_down():
    p.set_volume(p.current_volume()-1)
def pause():
    global t
    s=p.state()#取得当前播放状态0，表示没有音频；1，表示有音频，但没有输出，即停止；2，正在播放；3，正在录音。
    if s==2:
        t=p.current_position()#取得当前播放状态
        p.stop()
    elif s==1:
        p.set_position(t)#设置当前播放位置
        p.play()
m.bind(63497,vol_up)#绑定上为增加音量，详见快捷键的设置一节
m.bind(63498,vol_down)#绑定下为减少音量
m.bind(63557,pause)#绑定确定为暂停播放键
appuifw.app.menu=[(cn("选择歌曲"),play)]
e32.Ao_lock().wait()

#若路径中含中文，要加上“.decode("utf8")”，如："c:\\老人与海.mp3".decode("utf8")
