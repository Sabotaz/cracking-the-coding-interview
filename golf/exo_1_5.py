def _(a,b):
 t=False;x=len(a)-len(b);u=range(len(b))
 if x==-1:a,b=b,a
 if x==1:
  for i in u:
   if a[i]!=b[i]:return a[i+1:]==b[i:]
  t=True
 elif x==0:
  for i in u:
   if a[i]!=b[i]:return a[i+1:]==b[i+1:]
  t=True
 return t