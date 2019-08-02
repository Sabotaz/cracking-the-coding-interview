def _(s):
 l=set()
 for c in s:l^={c}-{" "}
 return len(l)<2