import sys, e32, appuifw
lock = e32.Ao_lock()
def myexitfunc():
  s = appuifw.app.screen
  appuifw.app.screen = 'large'
  appuifw.app.screen = s
  loc.wait()
sys.exitfunc = myexitfunc

#挂机键后台，C键无法退出


'''
import sys, e32
lock = e32.Ao_lock()
sys.exitfunc = lock.wait

#按红键后台运行
'''
