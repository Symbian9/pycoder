import telephone,e32
telephone.dial("10086")#拨打10086
e32.ao_sleep(5)
telephone.hang_up()#挂机


import messaging
def cn(x):return x.decode("utf8")
messaging.sms_send("10086","1")
#发送1到10086
messaging.sms_send("10086",cn("你好"),encoding="USC2")
#发送“你好”到10086
messaging.mms_send("10086",cn("你好！"),attachment="e:\\1.jpg")
#发彩信给10086，内容为“你好”，附件路径为“e:\\1.jpg”
