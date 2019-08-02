def URLify(sb, l):
    s=len(sb)
    for i in range(l, 0, -1):
        c = sb[i-1]
        if c == " ":
            sb[s-3:s] = "%20"
            s = s-3
        else:
            sb[s-1] = c
            s = s-1
    return sb
