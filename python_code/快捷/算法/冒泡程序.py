ar=[9,5,8,2,4,3]
l=len(ar)
for i in range(0,l):
  for j in range(0,l-i-1):
    if ar[j]>ar[j+1]:
      ar[j]=ar[j]+ar[j+1]
      ar[j+1]=ar[j]-ar[j+1]
      ar[j]=ar[j]-ar[j+1]
for i in range(0,l):
  print ar[i]