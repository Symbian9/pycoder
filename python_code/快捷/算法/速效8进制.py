#8bit进制转换

def hex2bin(a=0xff):
  for i in range(7,-1,-1):
    print a>>i&1,
def bin2hex(a='10000000'):
  b=0
  for i in a:
    b=b<<1|int(i)
  print hex(b)