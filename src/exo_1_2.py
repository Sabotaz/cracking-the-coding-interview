def is_permutation(s, t):
    return len(s) == len(t) and sorted(s) == sorted(t)
