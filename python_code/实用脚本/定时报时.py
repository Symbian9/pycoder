#定时停止循环
import time,e32,audio
def a():
    global run
    print '停止循环，定时循环已结束…'.decode('u8')
    run=0
    audio.say('停  止  计  时  循  环')
run=1
audio.say('开  始  计  时  循  环')
while run:
    time.sleep(1)
    e=time.strftime('%M')
    d=time.strftime('%H')
    m=time.strftime('%S')
    t='北京时间：'.decode('u8')
    u=d+':'+e+':'+m
    v=t+u
    print v
    if u=='20:31:00':
        a()
    e32.ao_yield()