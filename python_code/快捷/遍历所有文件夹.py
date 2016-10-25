import os
def walk(a,d,files):
  for i in files :
    if i[-4:]==".jpg":
      print i.decode("utf-8")
os.path.walk("e:\\",walk,None)