import appuifw
def cn(x):return x.decode("utf8")
a=appuifw.query(cn("请输入文字。"),"text")

#如果将text改为number,date,time,code，就是分别请求输入数字、日期、时间和密码。将text改为"query"，就是请求用户确认。如果用户按是，a等于1；按否，a等于0。