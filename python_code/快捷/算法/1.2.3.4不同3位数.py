#有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
#程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列
import appuifw
list=[]
for i in [1,2,3,4]:
  for j in [1,2,3,4]:
    for k in [1,2,3,4]:
      if(i!=k and i!=j and j!=k):
        list.append(str(i)+u''+str(j)+u''+str(k))
print list#输出三位数
print len(list)#输出个数