import appuifw
rest01 = '\\\\'.join(appuifw.app.full_name().split('\\'))
rest02 = open('d:\\restart.py', 'w')
rest02.write((u"import e32\ne32.ao_sleep(1.5)\ne32.start_exe('%s','')" % rest01))
rest02.close()
appuifw.e32.start_server('d:\\restart.py')
os.abort()

'''
二版的
import appuifw
rest01 = '\\\\'.join(appuifw.app.full_name().split('\\'))
rest02 = open('d:\\restart.py', 'w')
rest02.write((u"import e32\ne32.ao_sleep(1.5)\ne32.start_exe('z:\\\\system\\\\programs\\\\apprun.exe','%s')" % rest01))
rest02.close()
appuifw.e32.start_server('d:\\restart.py')
os.abort()
'''