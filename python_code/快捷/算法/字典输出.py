d={"bbb":2,"ssss":222,"due":333,"nv":1,"wxs":31,"ssksk":1,"kskdfkj":1,"kdsfk":2,"ke":222,"sdfkss":23}
t=d.iteritems()
l=[(i[1],i[0]) for i in t]
l.sort()
for i in l:
  print i[1],i[0]