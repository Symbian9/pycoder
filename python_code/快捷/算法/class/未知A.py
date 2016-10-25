class Sum:
  def __init__(self, sid,cid):
    self.sid = sid
    self.cid = cid
  def demoSum(self, bid):
    sumNumber = self.sid + self.cid + bid
    return sumNumber
  def mytest(self,tid):
    return self.demoSum(tid)
if __name__ == '__main__':
  test = Sum(5, 6)
  print test.demoSum(10)
  print test.mytest(2)

#当你执行这个脚本时，if __name__ == '__main__': 下面的代码会被执行，当这个脚本被 import 的时候if __name__ == '__main__': 下面的代码是不会被执行的。所以if __name__ == '__main__': 下面的东西可以写测试脚本，只有直接执行才能运行，不影响import。就相当于做小的单元测试