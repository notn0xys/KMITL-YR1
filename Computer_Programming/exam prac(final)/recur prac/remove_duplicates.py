def remove_duplicates(s,r = ""):
    if len(s) == 0:
        return r
    if s[0] not in r:
        r += s[0]
    return remove_duplicates(s[1:],r)
print(remove_duplicates("abcabc"))