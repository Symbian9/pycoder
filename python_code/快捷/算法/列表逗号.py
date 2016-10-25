a=['1','2,3','4']
a.insert(1,a[1].split(',')[0])
a.insert(2,a[2].split(',')[1])
del a[3]
print a