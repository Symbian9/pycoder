

a=['F-' + str(x) for x in range(4)]

b=['-'.join(i) for i in zip(['F'] * 4, 
[str(j) for j in range(1,5)])]

c=['F-%d' %x for x in range(1,5)]

print a,b,c