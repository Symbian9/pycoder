import sys
sys.path.append("E:\System\Apps\LexunUBBEdit")
try:
    import LexunUBBEdit
except:
    import traceback
    import sys
    import appuifw
    appuifw.app.body=body=appuifw.Text()
    appuifw.app.menu=[(u'\u9000\u51fa',sys.exit)]
    (type, value, tb) = sys.exc_info()
    tblist = traceback.extract_tb(tb)
    list = traceback.format_list(tblist)
    list[len(list):] = traceback.format_exception_only(type, value)
    body.color=0xff0000
    body.add(u''.join(list))
