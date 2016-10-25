
import os
os.sep#可以取代操作系统特定的路径分割符。
os.name#字符串指示你正在使用的平台。
os.getcwd()#函数得到当前工作目录，即当前Python脚本工作的目录路径。
#os.getenv()
#os.putenv()
#函数分别用来读取和设置环境变量。
os.listdir()#返回指定目录下的所有文件和目录名。
os.remove()#函数用来删除一个文件。
os.system()#函数用来运行shell命令。
os.linesep#字符串给出当前平台使用的行终止符。
os.path.split()#函数返回一个路径的目录名和文件名。
os.path.isfile()
os.path.isdir()
#函数分别检验给出的路径是一个文件还是目录。
os.path.existe()#函数用来检验给出的路径是否真地存在

os.listdir(dirname)#列出dirname下的目录和文件
os.getcwd()#获得当前工作目录
os.curdir#返回但前目录（'.')
os.chdir(dirname)#改变工作目录到dirname
os.path.isdir(name)#判断name是不是一个目录，name不是目录就返回false
os.path.isfile(name)#判断name是不是一个文件，不存在name也返回false
os.path.exists(name)#判断是否存在文件或目录name
os.path.getsize(name)#获得文件大小，如果name是目录返回0L
os.path.abspath(name)#获得绝对路径
os.path.normpath(path)#规范path字符串形式
os.path.split(name)#分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
os.path.splitext()#分离文件名与扩展名
os.path.join(path,name)#连接目录与文件名或目录
os.path.basename(path)#返回文件名
os.path.dirname(path)#返回文件路径

