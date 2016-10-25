import sysinfo,appuifw,e32

def cn(x):return x.decode("utf8")
appuifw.app.body=t=appuifw.Text()
t.focus=False
appuifw.app.screen="full"
t.add(cn("情景模式：")+sysinfo.active_profile())
t.add(cn("\n电量：")+unicode(sysinfo.battery()))
t.add(cn("\n屏幕分辨率：")+unicode(sysinfo.display_pixels()))
t.add(cn("\n剩余空间：\n"))
i=0
drive=[u"C:",u"D:",u"E:"]
while i<len(drive):
  t.add(drive[i]+unicode(sysinfo.free_drivespace()[drive[i]]/1024)+u"kb\n")
  i+=1
t.add(cn("剩余运存：")+unicode(sysinfo.free_ram()/1024)+u"kb")
t.add(cn("\nIMEI：")+unicode(sysinfo.imei()))
t.add(cn("\n系统版本：")+unicode(sysinfo.os_version()))
t.add(cn("\n响铃方式：")+unicode(sysinfo.ring_type()))
t.add(cn("\n手机版本：")+unicode(sysinfo.sw_version()))
t.add(cn("\n缓存总大小：")+unicode(sysinfo.total_ram()/1024)+u"kb")
t.add(cn("\nZ盘总大小：")+unicode(sysinfo.total_rom()/1024)+u"kb")
t.add(cn("\n信号强度：")+unicode(sysinfo.signal_bars()))
t.add(cn("\n信号强度：")+unicode(sysinfo.signal_dbm())+u"dbm")

e32.ao_sleep(3)