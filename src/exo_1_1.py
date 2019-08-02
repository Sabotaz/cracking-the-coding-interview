def uniq(s):
    return len(set(s)) == len(s)

def uniq2(s):
    all = set()
    for i in s:
        if i in all:
            return False
        all.add(i)
    return True

def uniq3(s):
    # without additionnal datastructure
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True
