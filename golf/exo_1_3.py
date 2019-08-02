def _(b,l):
 s=0
 for c in b[l-1::-1]:
  s-=1;b[s]=c
  if" "==c:b[s-2:s+1]="%20";s-=2
 return b