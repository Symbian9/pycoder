M=[]#新建一个空列表
M.append("orange")
M.append("apple")#向列表中添加了两个元素
M.sort()#将两个元素按字母表顺序排序
M.remove("orange")#将列表中的orange元素删除
#M.insert("fish",2)#在第二个位置插入fish

#下面加一个将列表中所有string元素转化成unicode的方法
list=dir()
list1=[]
i=0
while i<len(list):
    list1.append(unicode(list[i]))
    i+=1
print list1,M
#list1就是我们需要的列表，我们可以把它作为列表界面的列表