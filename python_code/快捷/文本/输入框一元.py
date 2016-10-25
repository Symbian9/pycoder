import appuifw
def cn(x):return x.decode("utf8")
def a():
  y=appuifw.query(cn("请输入函数："),"text")
  if y==None:pass
  else:
    try:
      K=()
      for i in range(10):
        x=2*i
        c=eval(y)
        K+=(i,c)
      print K
    except:
      a()
a()