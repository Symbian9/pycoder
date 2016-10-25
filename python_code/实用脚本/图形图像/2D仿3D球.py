import appuifw,graphics,e32
running=1
def quit():
  global running
  running=0
canvas=appuifw.Canvas()
appuifw.app.body=canvas
appuifw.app.screen='full'
img=graphics.Image.new(canvas.size)
appuifw.app.exit_key_handler=quit
while running:
  img.clear(0)
#本课关键就这一句#效果的产生利用了色彩的渐变和叠加#这里循环60次即叠加60次
  for i in range(60):
#叠加对象是画点，大家可以想象一下，不同颜色深度的点叠在一??是不是有层次感和明暗变化呢？#这里正是利用了这个道理。#(100-i/2,100-i/2)这个改变圆心坐标，作用是改变聚光点，不让其出现在中心，更有立体感。#(i*4,i*4,i*4)填充色，为什么是这样呢？颜色渐变呗。(0,0,0)-->(255,255,255)纯黑到纯白，叠加之后灰度渐变效果#width=120-2*i，点的大小，这里为何要改变呢？对，就是要一点点的增大才能实在叠加，大小一样就没效果喽。#大家可以尝试修改这些参数
    img.point((100-i/2,100-i/2),(i*4,i*4,i*4),width=120-2*i)
#这个椭圆效果留给大家思考
  for i in range(30,1,-1):
    img.ellipse((105-5*i/2,15-i/3,105+3*i/2,15+i),fill=(0,265-8*i,265-8*i))
  canvas.blit(img)
  e32.ao_yield()