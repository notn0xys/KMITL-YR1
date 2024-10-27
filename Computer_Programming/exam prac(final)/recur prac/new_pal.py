def palindrome(s:str):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])
print(palindrome("racecarr"))