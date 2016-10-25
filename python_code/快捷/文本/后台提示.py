import appuifw
import e32
e32.ao_sleep(3)
#给你时间把ped切换到后台。
appuifw.note(u"helloworld", "info", 1)
#这样在待机，功能表，其它软件中都有提示
#appuifw.note(u"helloworld", "info", 0)
#这样在后台只能听到提示音