#https://leetcode.com/problems/valid-parentheses/submissions/1509001021/


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s
    while len(s) != 0:
        print(s)
        if "{}" in s:
            s =  s.replace("{}", "")
        elif "[]" in s:
            s = s.replace("[]", "")
        elif "()" in s:
            s = s.replace("()", "")
        else:
            return False
        
    return True




check = isValid("({([]))")
print(f"valid:{check}")

check = isValid("((")
print(f"valid:{check}")