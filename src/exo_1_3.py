def URLify(sb, l):
    s=len(sb)-1
    for i in range(l, 0, -1):
        c = sb[i-1]
        if c == " ":
            sb[s-2:s] = "%20"
            s = s-3
        else:
            sb[s] = c
            s = s-1
    return sb
