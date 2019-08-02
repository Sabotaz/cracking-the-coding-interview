def _(b,l):
 s=0
 for c in b[l-1::-1]:
  s-=1;b[s]=c
  if" "==c:s-=2;b[s:s+3]="%20"
 return b
