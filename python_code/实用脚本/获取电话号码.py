import logs
m=logs.calls(mode='missed')[0]
print m['number']
#获取最后拨出的电话/手机号码
m=logs.calls(mode='in')
for i in range(len(m)):
  print m[i]['number']
#获取通讯记录所有来电的电话/手机号码
m=logs.calls(mode='out')[0]
print m['number']
#获取最新拨出的电话/手机号码
m=logs.sms(mode='in')
for i in range(len(m)):
  print m[i]['number']
#获取收取短信的