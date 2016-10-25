a=""
for i in range(1,10):
  for j in range(1,i+1):
    a +="%s*%s=%s "%(j,i,i*j)
    if i==j:a +="\n"
print a