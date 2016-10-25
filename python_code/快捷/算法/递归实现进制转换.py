def xnum(s,n):
  if 0==s:return ''
  else:
    nr=xnum(s/n,n)
    num=s%n
    return nr+str(num)
print xnum(6,4)

#第一个需要转换的数，第二个进制数(若要转换成超过10进制的，请自己加if判断即可。