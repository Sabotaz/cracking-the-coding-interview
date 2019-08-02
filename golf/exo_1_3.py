def _(b,l):
 s=len(b)-1
 for i in range(l,0,-1):
  b[s]=c=b[i-1]
  if" "==c:b[s-2:s]="%20";s=s-2
  s=s-1
 return b