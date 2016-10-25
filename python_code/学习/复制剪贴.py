import appuifw2 as appuifw
import e32

def ru(x):
  return x.decode('utf-8')

def s_1():
    s_45.select_all()

def s_2():
    s_3 = appuifw.query(ru('开始位置：'),'number',s_45.get_selection()[0]-1)
    if s_3 == None or s_3 == len(s_45):
        return
    s_4 = appuifw.query(ru('结束位置：'),'number',s_45.get_word_info()[1]-1)
    if s_4 == None or s_4 == len(s_45):
        return
    if s_3 == s_4:
        return
#    if s_4 
    s_45.set_selection(pos=int(s_3),anchor=int(s_4))
#    s_45.set_selection(pos=3,anchor=10)

def s_5():
    if len(s_45.get_selection()[2]) == 0:
        appuifw.note(ru('未标记文字！'), 'error')
    else:
        s_45.cut()

def s_7():
    if len(s_45.get_selection()[2]) == 0:
        appuifw.note(ru('未标记文字！'), 'error')
    else:
        s_45.copy()

def s_8():
    s_45.paste()

def s_6():
    s_9 =  appuifw.popup_menu([ru('字母'),ru('数字'),ru('默认')],ru('输入模式'))
    if s_9 == None:
        return
    if s_9 == 0:
        s_45.set_input_mode(appuifw.EHalfWidthTextInputMode)
    if s_9 == 1:
        s_45.set_input_mode(appuifw.ENumericInputMode)
    if s_9 == 2:
        s_45.set_input_mode(appuifw.ENullInputMode)



def edit_callback(pos, num):
    appuifw.app.title = ru('字数: ')+unicode(len(s_45.get()))
    s_45.indicator_text = unicode(len(s_45.get()))

appuifw.app.body = s_45 = appuifw.Text(edit_callback=edit_callback,scrollbar=True)
s_45.color = (0, 0, 255)
s_45.font = ('dense', 18)

appuifw.app.menu = [(ru('切换'),s_6),(ru('标记'),((ru('全选'),s_1),(ru('自定'),s_2))),(ru('模板'),((ru('复制'),s_7),(ru('剪切'),s_5),(ru('粘帖'),s_8)))]

lock = e32.Ao_lock()

appuifw.app.exit_key_handler = lock.signal

lock.wait()