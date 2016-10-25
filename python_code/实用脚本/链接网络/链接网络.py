import appuifw as ui
import httplib
from os import abort
uia=ui.app
uin=ui.note
uiq=ui.query
e32=ui.e32
socket=httplib.socket
def cn(x):return x.decode('utf8')
uia.body=txt=ui.Text()
global dic
dic={'p':''}
run=1

def ou(url,ret=1):
  #socket.access_point(dic['p']).start()
  con=httplib.HTTPConnection('10.0.0.172',80)
  con.putrequest('GET',url)
  con.putheader('Accept','*/*')
  con.endheaders()
  if ret:
    r=con.getresponse()
    data=cn(r.read())
    con.close()
    return data
  else:
    con.close()
    return 

def quit():
  if uiq(cn("是否退出程序？"),"query"):
    if lock:
      lock.signal()
    else:
      abort()
name=uia.full_name().split('\\')[-1][:-4].lower()
if name in ['ped','appmgr']:
  lock=e32.Ao_lock()
else:
  lock=None
def stop():
  global run
  run=0
  uia.title=cn('已经停止!')


def start():
  run=1
  global run
  a1=0
  while run:
    a1+=1

    uia.title=cn('第%s次'%a1)
    try:
      da=ou('http://3g.qq.cn')
      txt.set(da[200:400])
      uia.title=cn('第%s次'%a1)
      da=ou('http://wap.ucweb.com')
      txt.set(da[200:400])
    except: pass
    e32.ao_sleep(2)


uia.exit_key_handler=quit
def main():
  uia.menu=[(cn('开始'),start),(cn('停止'),stop),(cn('退出'),quit)]

  if lock:
    lock.wait()
if 1:
  uin(cn("请选择CMWAP接入点"))
  dic['p']=socket.select_access_point()
  txt.set(cn('\t网络测试中...%s'%str(dic['p']).encode('hex')))
  try:
    ou('http://3gsoft.5wap.net')
    uin(cn('网络测试成功'))
  except:
    uin(cn('网络测试失败'))
txt.set('')
main()