#capitalize将第一个字母转为大写
STR = 'python.t x t'
print STR.capitalize()

#center以空格补位(左右两侧)
print STR.center(15)

#count单一字符数量，()内容[字符(必填),开始位置(可选),结束位置(可选)]（区分大小写)
print STR.count('p')

#endswith判断字符中是否带后缀名(有返1冇返0)
print STR.endswith('txt')

#expandtabs把字符中的标签字符替换没空格，默认是8个
print STR.expandtabs()

#find查找字符，()内三个参数［字符（心填），开始位置（可选），结束（可选）］冇返回-1,有返回位置(区分大小写)
print STR.find('h',0,6)

#index查找字符，和find一样，不一样的是冇返回异常print STR.index('p',0)

#isalnum判断字符是否全为字母和数字，(是返回1,否返回0)
print STR.isalnum()

#isalpha判断字符是否全为字母，(是返回1,否返回0)
print STR.isalpha()

#isdigit判断字符是否全为数字，(是返回1,否返回0)
print STR.isdigit()

#islower判断字符中的字母是否全为小写，(是返回1,否返回0)
print STR.islower()

#isspace判断字符是否全为空白字符，(是返回1,否返回0)
print STR.isspace()

#istitle判断字符中的首字母是否为大写，(是返回1,否返回0)
print STR.istitle()

#isupper判断字符是否全为大写，(是返回1,否返回0)
print STR.isupper()

#join将列表连接成字符
print ''.join(['pyt','ho','n'])

#ljust以空格补位(后)
print STR.ljust(15)

#lower将字符转为小写
print STR.lower()

#lstrip删除字符串前面的字符(我也不知道怎么说)看示例
print STR.lstrip('p')
#p是第一个，不能删除y因为前面有个p,只能STR.lstrip('py')

#replace替换，()内容[被替换内容(必填)，替换内容(必填)，替换个数(可选)]
print STR.replace('.',',')

#rfind反向查找,和find一样，不同的是向后面开始查找
print STR.find('t')
print STR.rfind('t')

#rindex反向查找，和index一样，不同的是向后面开始查找（冇返回异常）
print STR.rindex('t')

#rjust以空格补位(前)
print STR.rjust(15)

#rstrip删除字符串后面的字符，lstrip的反面
print STR.rstrip('t')

#split将字符串分割成列表(默认分割字符为空格既' ',次数可选默认分割全部)
print STR.split(' ',1)

#splitlines按行分割字符,发现个有趣的问题（）内竟是可选布耳值，True:保留换行符，False:不保留换行符！
print STR.splitlines(False)

#startswith判断字符串的开头（字符，可选参数开始int型，可选参数结束int型）（是返回1，否返回0）
print STR.startswith('p',0,12)

#strip和rstrip，lstrip差不多，不一样的是这个函数是删除前后的字符
A='pythonp'
print A.strip('p')

#swapcase字母大小写互换
print STR.swapcase()

#title将首字母转为大写其他为小写，非字母分开则被默认为开头
print STR.title()

#translate大概是产生翻译表之类的

#upper将字符转为大写
print STR.upper()

#zfill以0向右补全
print STR.zfill(15)