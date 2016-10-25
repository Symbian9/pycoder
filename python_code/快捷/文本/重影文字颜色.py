import appuifw,os,e32
#载入appuifw,os,e32这三个模块

appuifw.app.body=appuifw.Text()
#定义一个文本显示页面

appuifw.app.body.style=eval('appuifw.HIGHLIGHT_SHADOW')
#把显示文字定义成重影。

def ru(x): return x.decode('utf-8')
#涵数，使decode('utf-8')编码方便使用。
colors=appuifw.query(ru('输入颜色的 RGB 值'),'text', u'255, 0, 255')
#输入颜色的RGB值。《主色》

#colors=u'255,0,255'#预先规定显示颜色的RGB值，不用输入。


if len(colors)>=0:
	#判断是否有输入内容，可不用，但不用的话，如果输入时按取消，某些机型会报错《系统错误》
	appuifw.app.body.color = eval('('+colors+')')
	#定义主色。《非重影背后的颜色》

highlight_colors=appuifw.query(ru('输入补充色的 RGB 值'),'text', u'0, 255, 0')
#输入颜色的RGB值。《用于重影》

#highlight_colors=u'0,255,0'#预先规定重影显示颜色的RGB值，不用输入。

if len(highlight_colors)>=0:
	#判断是否有输入内容，可不用，但不用的话，如果输入时按取消，某些机型会报错《系统错误》。
	appuifw.app.body.highlight_color = eval('('+highlight_colors+')')
	#定义重影后面文字的颜色。

lock=e32.Ao_lock()
os.abort=lock.signal
lock.wait()
#停止先前模块的使用。在解释器状态下，重新定义了一个文字显示页面，就需要加上这句，否则会立即返回解释器。
#by 无恋