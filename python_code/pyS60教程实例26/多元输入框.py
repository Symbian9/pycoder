import appuifw
(a,b)=appuifw.multi_query(u"text1",u"text2")

#a,b分别是用户输入的两个值。输入文字系统会直接转换为“unicode”代码。按“否”，系统会报错。可改为下面的形式a=appuifw.multi_query(u"text1",u"text2")按否则返回0。输入后按是，返回一个二元序列。