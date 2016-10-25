#OK键射击

import appuifw
import graphics
import e32
import random
import key_codes

da=50
ge=7
time=100.0

w = 40
h = 15
clo = (12, 116, 204)
shu = 7
ticlo = (255, 0, 0)
TIME = 10000

def hua(rect):
        global shoot, sleep, ufos, timer
        buf.clear((0, 0, 0))
        buf.rectangle((pad_x, H - h, pad_x + w, H),\
                fill = clo)

        if shoot:
                x = pad_x + w / 2
                buf.line((x, H - h, x, 0),\
                        width = 2, outline = ticlo)
                shoot = False
                sleep = 0.1
                check_hits(x)
        else:
                sleep = 0.01
        
        for x, y, s, t, hit in ufos:
                f = 1.0 - (timer - t) / time
                if hit:
                        c = (255, 0, 0)
                else:
                        c = (0, f * 255, 0)
                buf.ellipse((x, y, x + s, y + s), fill = c)

        buf.text((10, 40), u"%d" % score,
                fill = ticlo, font = "title")
        
        buf.text((W - 70, 40), u"%d" % (TIME - timer),
                fill = ticlo, font = "title")
        
        canvas.blit(buf)


def check_hits(laser_x):
        global ufos, score
        i = 0
        ok_ufos = []
        for x, y, s, t, hit in ufos:
                if laser_x > x and laser_x < x + s:
                        ok_ufos.append((x, y, s, t, True))
                        score += da - (s - 1)
                else:
                        ok_ufos.append((x, y, s, t, False))
        ufos = ok_ufos

def update_ufos():
        global ufos, timer
        ok_ufos = []
        for x, y, s, t, hit in ufos:
                if not hit and timer < t + time:
                        ok_ufos.append((x, y, s, t, False))
        ufos = ok_ufos
        
        if len(ufos) < ge:
                s = random.randint(10, da)
                x = random.randint(0, W - s)
                y = random.randint(0, H - h * 3)
                t = random.randint(0, time)
                ufos.append((x, y, s, timer + t, False))


def handle_event(event):
        global direction, shoot
        if event['keycode'] == key_codes.EKeyLeftArrow:
                direction = -shu
        elif event['keycode'] == key_codes.EKeyRightArrow:
                direction = shu
        elif event['keycode'] == key_codes.EKeySelect:
                shoot = True

def quit():
  global timer
  timer = TIME
  appuifw.app.set_exit()

ufos = []
shoot = False
direction = pad_x = score = timer = 0
appuifw.app.exit_key_handler = quit
appuifw.app.screen = 'large'
canvas = appuifw.Canvas(event_callback = handle_event,\
                        redraw_callback = hua)
W, H = canvas.size
buf = graphics.Image.new((W, H))
appuifw.app.body = canvas 

while timer < TIME:
        pad_x += direction
        pad_x = min(pad_x, W - w)
        pad_x = max(pad_x, 0)

        update_ufos()
        hua((W, H))
        e32.ao_sleep(sleep)
        timer += 1

