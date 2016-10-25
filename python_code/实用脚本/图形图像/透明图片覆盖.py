class Transparent:
 bg_image=None//背景图片
 fg_image=None//上面透明的图片
 alpha=0.5//透明度
 def __init__(self,fg_img,bg_img,alpha):
  import appuifw,graphics
  self.bg_image=fg_img
  self.fg_image=bg_img
  self.alpha=alpha
 def makeTransparent(self):
  width1,height1=self.bg_image.size
  width2,height2=self.fg_image.size
  width=min(width1,width2)
  height=min(height1,height2)
  for x in range(width):
   for y in range(height):
    orginal_color1=self.bg_image.getpixel((x,y))[0]
    orginal_color2=self.fg_image.getpixel((x,y))[0]
    red1=orginal_color1[0]
    green1=orginal_color1[1]
    blue1=orginal_color1[2]
    red2=orginal_color2[0]
    green2=orginal_color2[1]
    blue2=orginal_color2[2]
    red=self.alpha*red1+red2*(1-self.alpha)
    green=self.alpha*green1+green2*(1-self.alpha)
    blue=self.alpha*blue1+blue2*(1-self.alpha)
    self.bg_image.point((x,y),(red,green,blue),width=1)
  return self.bg_image
 def __del__(self):
  self.image1=None
  self.image2=None
import graphics
img1=graphics.Image.open("e:\\bg_image.jpg")
img2=graphics.Image.open("e:\\fg_image.jpg")
p=Transparent(bg_image,fg_image,0.3)
img=p.makeTransparent()
img.save("e:\\transparent.jpg")