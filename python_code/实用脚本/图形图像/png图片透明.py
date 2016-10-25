def automask(im):
  #获得图片的宽和高
  width, height = im.size
  #记得将过，这个是新建一个图像，’1’表示生成黑白图像
  mask = Image.new(im.size, '1')
  #getpixel()函数返回像素(0,0)表示图像最左上角#因其返回的是列表所以取[0]
tran=im.getpixel((0,0))[0]
#循环所有点
for y in range(height):
  #获得某一高度的所有点像素#[(x,y) for x in range(width)]#即y固定，x取遍所有width，这样构成一个列表
line = im.getpixel([(x, y) for x in range(width)])
#现在line是一个列表，所以循环每个点
for x in range(width):
  #判断每个x像素是否和左上角的像??相同
if line[x] == tran:
  #相同则涂黑，画黑点mask.point((x,y), 0)#循环完毕，返回mask#这样就获得了mask
return mask
mask=automask(img)
#只能讲到这种地步了。我没研究过，呵呵~望大家见谅。#慢慢研究琢磨吧。不过你也可直接调用函数