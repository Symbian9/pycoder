a=6.150
b="琳琳的生日：".decode("u8")
print b+str(a)[:4]
print "%s%0.2f"%(b,a)
print "%s"%"lslczq"#格式化字符串
print "%d"%6.15#替换的值为整型
print "%f"%6.15#格式化浮点数精度，默认为6位
print "%0.1f"%6.15#保留一位
print "%c"%65#格式化字符及其ascⅡ码
print "%X"%615#无符号十六进制数
print "%e"%615#科学计数法格式化浮点数
print "%u"%615#无符号十进制数