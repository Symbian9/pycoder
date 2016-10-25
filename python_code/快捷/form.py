import appuifw
def ru(x):return x.decode('utf-8')

list0=[ru('好地方！'),ru('太强了！')]
a_little_list=[(ru('开花区'),'combo',(list0,1))]

my=appuifw.Form(a_little_list, appuifw.FFormDoubleSpaced)
my.execute()
a = []
for index in range(0, len(my), 1):
  index_list = my[index][2][1]
  a.append(my[index][2][0][index_list])

(c,) = a
if c==u'\u597d\u5730\u65b9\uff01':
  printout=0
else :
  printout=1

print printout