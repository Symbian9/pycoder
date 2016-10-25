import camera,appuifw,e32
appuifw.app.body=c=appuifw.Canvas()
def quit():
  camera.stop_finder()
  camera.release()
  lock.signal()
def see(im):
  c.blit(im,(0,0),(24,20))
camera.start_finder(see,size=(128,132))
appuifw.app.exit_key_handler = quit
lock=e32.Ao_lock()
lock.wait()

#c.blit(im,(0,0),(24,20))后面有两数组(tuple可能有人叫法不同)！意思是源图象的左上角坐标，Blit后的坐标！这个坐标可以是一个意思是左上角，可以是两个，就是对角了，本例中用一个！start_finder(see,size=(128,132))这句就是取景大小了，size=设定值！我设定的是128*132实际上取的是128*96，如果你设的是176*96，它还是取128*96，它会自动取小的一个数自动按比例缩放