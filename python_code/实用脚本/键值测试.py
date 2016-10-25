import keycapture
import e32,appuifw
import key_codes
import appswitch
s60_version=e32.s60_version_info[0]
if s60_version==3:
  from envy import set_app_system
  set_app_system(1)

appname=appswitch.application_list(0)[0]
key=[]
for i in dir(key_codes):
    if i.startswith('E'):
        key.append(eval('key_codes'+'.'+i))
rung=1
class Key:
  def __init__(s):
    s.press=keycapture.KeyCapturer(s.key_callback)
    s.press.keys=(key)
  def start(s):
    s.press.start()
  def key_callback(s,key):
    global rung
    print key
    if key==8:
        rung=0
        print 'Exit'
        s.press.stop()
k=Key()
k.start()
print 'Press "C " Key Exit'
while rung:
    if appswitch.application_list(0)[0]!=(appname):
        e32.ao_sleep(0.2)
        appswitch.switch_to_fg(appname)
    e32.ao_sleep(0.1)

