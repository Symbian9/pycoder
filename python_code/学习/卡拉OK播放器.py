#草木灰

import appuifw
import e32
import os

def zh(x):
    return x.decode("utf8")
def en(x):
    return x.encode("utf8")

def errors(errors_ = ""):
    appuifw.note((zh("加载%s模块失败！\n5秒后程序退出！") % errors_), "error", 1)
    e32.ao_sleep(5)
    appuifw.app.set_exit()

try:
    import powlite_fm
except:
    errors("powlite_fm")

try:
    import e32dbm
except:
    errors("e32dbm")

try:
    import audio
except:
    errors("audio")

global m
appuifw.app.body = m = appuifw.Text()
appuifw.app.title = zh("卡拉ok录音"
)
def file_1():
    path=powlite_fm.manager().AskUser("e:\\Sounds\\",ext=[".mp3",".wma",".wav"])
    global file_m
    file_m=audio.Sound.open(path)
    file_m.play()

def play():
    file_m.play()
    appuifw.app.menu = [
        (zh("选择歌曲播放"),file_1),
        (
            zh("播放选项"),
            (
                (zh("播放/暂停"),pause),
                (zh("停止"),stop),
                (zh("录音"),record)
            )
        )
    ]

def pause():
    global time    
    global status
    status = file_m.state()
    if (status == 2):
        time = file_m.current_position()
        file_m.stop()
    if (status == 1):
        try:
            file_m.set_position(time)
            file_m.play()
        except:
            appuifw.note(zh("无法继续播放"),"error")



def stop():
    file_m.stop()
    appuifw.app.menu = [(zh("继续播放"),play),(zh("重新选曲"),file_1)]

def recording(Name="record_new",file_path="e:\\Sounds\\"):
    path_r = audio.Sound.open(("%s%s.wav")%(file_path,Name))
    if appuifw.query(zh("是否需要原音乐伴唱？"),"query"):
        path_r.record()
        file_1()

        def stop_rf():
            path_r.stop()
            file_m.stop()
            Name = en(appuifw.query(zh("请输入名称："),"text"))
            appuifw.note(zh("请选择保存路径"),"info")
            file_path = powlite_fm.manager().AskUser(path = "e:\\",find = "dir")
            appuifw.note(zh("保存成功！"),"conf")

        def stop_f():
            file_m.stop()

        def stop_r():
            Name = en(appuifw.query(zh("请输入名称："),"text"))
            appuifw.note(zh("请选择保存路径"),"info")
            file_path = powlite_fm.manager().AskUser(path = "e:\\",find = "dir")
            appuifw.note(zh("保存成功！"),"conf")
        appuifw.app.menu = [(zh("保存录音"),stop_rf),(zh("停止录音"),stop_r),(zh("停止音乐"),stop_f)]


    else:
        path_r.record()
        def stop_r2():
            Name = en(appuifw.query(zh("请输入名称："),"text"))
            appuifw.note(zh("请选择保存路径"),"info")
            file_path = powlite_fm.manager().AskUser(path = "e:\\",find = "dir")
            appuifw.note(zh("保存成功！"),"conf")
        appuifw.app.menu = [(zh("保存录音"),stop_r2)]
        

appuifw.app.menu = [
    (zh("选择歌曲播放"),file_1),
    (
        zh("播放选项"),
        (
            (zh("播放/暂停"),pause),
            (zh("停止"),stop),
            (zh("录音"),recording)
        )
    )
]



lock=e32.Ao_lock()
appuifw.app.exit_key_handler=lock.signal
lock.wait()
