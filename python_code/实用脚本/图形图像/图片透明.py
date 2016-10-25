from graphics import *
import appuifw as ap,e32
ap.app.screen="full"
img=Image.open(u"***\\a.jpg")
img2=Image.new((240,320),"1")
#新建一张大小为(240x320)的图像，看到里面的那个参数"1"了吗？1为黑色，有了它才能整出透明来。
img2.load("***\\1.jpg")
#载入一张你需要它透明的图片(注意这张图片的大小一定要跟你刚刚新建的那张图像大小一样，否则出错)。这张处理透明后是黑白的。
ap.app.body=canvas=ap.Canvas()
canvas.blit(img,mask=img2)
#透明关键在于括号里的mask，你模仿就是了。石头提供的用法

e32.ao_sleep(10)