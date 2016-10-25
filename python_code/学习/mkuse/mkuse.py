'''
作者：爱不只是说说
联系QQ：337659907
模块简介：
     此模块主要用于查询常用模块的使用方法，尤其是对刚学习py的新手特别有帮助，用法也非常简单，并且你可以随时添加、修改模块的用法文档(用法文档与模块在同一文件夹(mkuse))，用的时候只需输入文件名即可导出！
模块用法：
      import mkuse
      print mkuse.love('os').decode('utf8')#输出os模块的用法，没有则返回None
      
      print mkuse.love(list)#输出模块用法列表
      
      print mkuse.love(len)#输出模块用法数量
      
      print mkuse.love()#输出模块用法信息
添加用法：
      如：添加e32模块的用法，编辑好文本后保存为'e:\\system\\libs\\mkuse\\e32.txt'即可！调用时只需mkuse.love('e32')便可导出！
其它说明：
      本模块用法均收集整理于WAPE乐社区和乐讯py论坛！模块用法中的作者仅代表编写模块用法的作者，不完全是模块的制作者！部分用法未注明作者是因为此用法已收集很久一时记不清作者昵称，故没填写！

如有其它的意见建议或模块使用方法欢迎联系本人！

爱不只是说说发布于2009/05/05
'''

import os,mkuse

path=os.path.split(mkuse.__file__)[0]+'\\'
del mkuse

def love(name=''):
  if name:
    if name==list:
      return os.listdir(path)
    elif name==len:
      return len(os.listdir(path))-2
    else:
      if os.path.exists(path+name+'.txt'):
        a=open(path+name+'.txt','r')
        return a.read()
        a.close
      else:
        return 'None'
  else:
    return __doc__

if __name__=='__main__':
  print love().decode('utf8')
