class img_fx:
    def fx(self,img,x,y,save_img):
        import appuifw,e32,graphics
        img2=graphics.Image.new((x,y))
        img0=img.resize((x,y))
        for i in range(y):
            for j in range(x):
                t=img.getpixel((j,i))[0]
                img2.point((x-j,i),t,width=1)
                e32.ao_yield()
        img2.save(save_img)
import graphics
img = graphics.Image.open('e:\\s.png')
img_fx().fx(img,176,208,'e:\\m0.png')