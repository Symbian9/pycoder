import threading
import time

class XinThread(threading.Thread):
    def __init__(self, num):
        #super(XinThread, self).__init__()
        threading.Thread.__init__(self)
        self.num = num
        self.create_time = time.time()

    def run(self):
        time.sleep(1)
        print("线程", self.num, "被创建")
        print(time.time() - self.create_time)
        print("线程", self.num, "结束")


for item in range(7):
    t = XinThread(item)
    t.start()



input()
