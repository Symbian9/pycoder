#代码源自泡椒池塘阿斌作，经tengge修改而成。请先在e盘根目录下弄一张名为“1.jpg”的图片，再运行该代码。

import appuifw,e32
from graphics import *

appuifw.app.body=ca=appuifw.Canvas()
appuifw.app.screen="full"
img=Image.open("e:\\1.jpg")
#引入图片，打开现有图片

img1=img.resize((80,90))
#重设图片大小
img2=img1.transpose(FLIP_LEFT_RIGHT)
#左右翻转
img3=img1.transpose(FLIP_TOP_BOTTOM)
#上下翻转
img4=img1.transpose(ROTATE_90)
#逆时针翻转90度
img5=img1.transpose(ROTATE_180)
#逆时针翻转180度
img6=img1.transpose(ROTATE_270)
#逆时针翻转270度

img2.save("e:\\2.jpg")#保存图片

def redraw(rect):
    ca.blit(img1)
    ca.blit(img2,target=(0,200))
    ca.blit(img3,target=(160,0))
    ca.blit(img4,target=(0,100))
    ca.blit(img5,target=(160,200))
    ca.blit(img6,target=(150,100))
redraw(())
e32.Ao_lock().wait()