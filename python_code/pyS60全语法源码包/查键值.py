#查键值
# keyviewer.py

import appuifw
import graphics
import e32

keyboard_state={}
last_keycode=0

def cn(x):return x.decode('utf-8')

def draw_state():
    canvas.clear()
    canvas.text((0,12),u'Scancodes of pressed keys:',0x008000)
    canvas.text((0,30),u' '.join([unicode(k) for k in keyboard_state if keyboard_state[k]]))
    canvas.text((0,50),u' '.join([unicode(hex(k)) for k in keyboard_state if keyboard_state[k]]))
    canvas.text((0,80),u'Last received keycode:', 0x0000ff)    
    canvas.text((0,100),cn(' %s        (%x   )')%(last_keycode,last_keycode))
    
def callback(event):
    global last_keycode
    if event['type'] == appuifw.EEventKeyDown:
        keyboard_state[event['scancode']]=1
    elif event['type'] == appuifw.EEventKeyUp:
        keyboard_state[event['scancode']]=0
    elif event['type'] == appuifw.EEventKey:
        last_keycode=event['keycode']
    draw_state()

canvas=appuifw.Canvas(event_callback=callback,
                      redraw_callback=lambda rect:draw_state())
appuifw.app.body=canvas

lock=e32.Ao_lock()
appuifw.app.exit_key_handler=lock.signal
lock.wait()
