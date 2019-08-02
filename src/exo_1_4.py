def is_palindrome_permutation(s):
    letters = set()
    for c in s:
        if c != " ":
            if c in letters:
                letters.remove(c)
            else:
                letters.add(c)

    return len(letters) <= 1
