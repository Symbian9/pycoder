
import sysinfo,appuifw,e32
#sysinfo是与系统信息有关的模块

def cn(x):return x.decode("utf8")

appuifw.app.body=t=appuifw.Text()
t.focus=False
appuifw.app.screen="full"

t.add(cn("情景模式：")+sysinfo.active_profile())#查看当前情景模式
t.add(cn("\n电量：")+unicode(sysinfo.battery()))#查看当前电量
t.add(cn("\n屏幕分辨率：")+unicode(sysinfo.display_pixels()))#查看屏幕分辨率
t.add(cn("\n剩余空间：\n"))
i=0
drive=[u"C:",u"D:",u"E:"]
while i<len(drive):#循环语句
    t.add(drive[i]+unicode(sysinfo.free_drivespace()[drive[i]]/1024)+u"kb\n")#查看C,D,E盘剩余空间
    i+=1
t.add(cn("剩余运存：")+unicode(sysinfo.free_ram()/1024)+u"kb")#查看剩余运存
t.add(cn("\nIMEI：")+unicode(sysinfo.imei()))#查看手机串号
t.add(cn("\n系统版本：")+unicode(sysinfo.os_version()))#查看系统版本信息
t.add(cn("\n响铃方式：")+unicode(sysinfo.ring_type()))#查看响铃方式
t.add(cn("\n手机版本：")+unicode(sysinfo.sw_version()))#查看手机版本
t.add(cn("\n缓存总大小：")+unicode(sysinfo.total_ram()/1024)+u"kb")#查看剩余缓存
t.add(cn("\nZ盘总大小：")+unicode(sysinfo.total_rom()/1024)+u"kb")#查看Z盘总大小

e32.Ao_lock().wait()
