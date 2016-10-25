import sys, traceback
def mytest():
  try:
    a = 1/0
  except:
    traceback.print_exc()
mytest()
print '-'*30