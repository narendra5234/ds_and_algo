# O(n^2) time|O(n) space
def is_palindrome(string):
    rev_str = ""
    for i in reversed(range(len(string))):
        rev_str += string[i]
    return string == rev_str


# O(n) time|O(n) space
def is_palindrome_2(string):
    rev_chars = []
    for i in reversed(range(len(string))):
        rev_chars.append(string[i])
    return string == "".join(rev_chars)


# O(n) time|O(n) space
def is_palindrome_3(string, i=0):
    j = len(string) - i
    return True if i >= j else string[i] == string[j] and is_palindrome_3(string, i + 1)


# O(n) time|O(1) space
def is_palindrome_4(string):
    l, r = 0, len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True
