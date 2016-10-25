import thread,e32
i=[0,0]
def a(x):
  k,i[1]=0,1
  while k<10000:
    if i[0]:
      i[1]=0
      thread.exit()
    print k,
    k+=1
def stop():
  i[0]=1
  e32.ao_sleep(0.01)#这儿必须要一段延迟
def query():
  if i[1]:print "Is running"
  else:print "Have stoped"
thread.start_new_thread(a,(1,))
e32.ao_sleep(1)
query()
e32.ao_sleep(1)
stop()#结束子线程
query()#查询线程状态