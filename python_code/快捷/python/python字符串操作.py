'''1.复制字符串'''
sStr1 ='aaaa'
sStr2 = sStr1
sStr1 ='bbbb'
print sStr2
#是复制哦
'''2.连接字符串'''
sStr1 ='strcat'
sStr2 ='append'
sStr1 += sStr2
print sStr1
'''3.查找字符'''
sStr1 ='strchr'
sStr2 ='r'
nPos = sStr1.index(sStr2)
print nPos
'''4.比较字符串'''
sStr1 ='strchr'
sStr2 ='strch'
print cmp(sStr1,sStr2)
#不相等，返回1
'''5.扫描字符串是否包含指定的字符'''
sStr1 ='12345678'
sStr2 ='456'
print len(sStr1 and sStr2)
'''6.字符串长度'''
sStr1 ='strlen'
print len(sStr1)
'''7.将字符串中的小写字符转换为大写字符'''
sStr1 ='JCstrlwr'
sStr1 = sStr1.upper()
print sStr1
'''8.追加指定长度的字符串'''
sStr1 ='12345'
sStr2 ='abcdef'
n = 3
sStr1 += sStr2[0:n]
print sStr1
'''9.字符串指定长度比较'''
#strncmp(sStr1,sStr2,n)
sStr1 ='12345'
sStr2 ='123bc'
n = 3
print cmp(sStr1[0:n],sStr2[0:n])
#相等返回0
'''10.复制指定长度的字符'''
sStr1 =''
sStr2 ='12345'
n = 3
sStr1 = sStr2[0:n]
print sStr1
'''11.字符串比较，不区分大小写'''
sStr1 ='abcefg'
sStr2 ='ABCEFG'
print cmp(sStr1.upper(),sStr2.upper())
'''12.将字符串前n个字符替换为指定的字符'''
sStr1 ='12345'
ch ='r'
n = 3
sStr1 = n * ch + sStr1[3:]
print sStr1
'''13.扫描字符串'''
sStr1 ='cekjgdklab'
sStr2 ='gka'
nPos = -1
for c in sStr1:
  if c in sStr2:
    nPos = sStr1.index(c)
    break
print nPos
#结果是2，即k在sStr2中存在，其在sStr1中的索引是2
'''15.查找字符串'''
sStr1 ='abcdefg'
sStr2 ='cde'
print sStr1.find(sStr2)
#返回'cde'在'abcdefg'中的偏移 2
'''16.分割字符串'''
sStr1 ='ab,cde,fgh,ijk'
sStr2 =','
sStr1 = sStr1.split(sStr2)
#结果是 ['ab', 'cde', 'fgh', 'ijk']print sStr1
'''17.连接字符串'''
lista = ['ab','cde','fgh','ijk']
x = ('-').join(lista)
print x