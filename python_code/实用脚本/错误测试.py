try:
  A
except:
  import traceback,sys
  txt = unicode(''.join(traceback.format_exception(*sys.exc_info())))
  print txt


import e32
e32.ao_sleep(5)