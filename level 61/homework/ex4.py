def is_palindrome(s):
    s = s.lower()
    if s[::-1] == s:
        return True
    return False