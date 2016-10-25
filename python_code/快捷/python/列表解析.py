# 普通列表解析by 飞影
print [(i*2) for i in range(8)]
# 带判断的列表解析--可以过滤不符合条件的元素
print [(i*2) for i in range(8) if i%2] # i%2为求余
# 矩阵列表解析--新手可能比较难理解，多试几次就可以明白了
print [(i,p) for i in range(2) for p in range(2,4)]
# 带判断的矩阵列表解析
print [(i,p) for i in range(4) if i%2 for p in range(2,6) if p%2]
# 多矩阵列表解析--比较少用，要理解得用点心思才行。
print [(i,p,v) for i in range(2) for p in range(2,4) for v in range(5,7)]