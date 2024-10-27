def is_palindome(s:str):
    return is_palindrome_helper(s,0)
def is_palindrome_helper(s:str,count = 0,expression = True):
    if expression == False:
        return False
    if count == len(s) // 2  :
        return expression
    else:
        if s[count] != s[len(s) - 1 - count]:
            return False
        else:
            count += 1
            return is_palindrome_helper(s,count,expression)
print(is_palindome("raceecar"))