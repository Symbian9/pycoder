
import os
os.listdir("e:\\")#列出某目录下的文件和文件夹
os.makedirs("e:\\tengge\\img\\")#新建路径
os.remove("e:\\tengge.txt")#删除文件
os.removedirs("e:\\tengge\\img\\")#删除空文件夹
os.rename("e:\\1.jpg","e:\\3.jpg")#重命名文件或文件夹
os.path.exists("e:\\tengge\\")#判断某路径是否存在
os.isdir("e:\\tengge")#判断是否是路径
os.isfile("e:\\tengge")#判断是否是文件
