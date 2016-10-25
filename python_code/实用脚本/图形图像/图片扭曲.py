class MakeTemp:
    def make(slef,img,X,Y,load):
        
        import graphics , e32 , appuifw
  
        width , height = img.size
        a = 0
        for y in range(height):
            for x in range(width):
                a = a + 0.001
                e32.ao_yield()
            e32.ao_yield()
        img2 = graphics.Image.new((width + a, height))
        a = 0
        for y in range(height):
            for x in range(width):
                a = a + 0.001
                t = img.getpixel((x,y))[0]
                img2.point((x+a,y),t)
                e32.ao_yield()
            e32.ao_yield()
        img3 = graphics.Image.new((x+a, height))
        img3.blit(img2)
        img3 = img3.resize((X,Y),keepaspect=1)
        img3.save(load)

import graphics
img = graphics.screenshot()
MakeTemp().make(img,240,320,'d:\\temp.jpg')