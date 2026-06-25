from solution import is_palindrome

# Basic cases
assert is_palindrome("")  # empty string is a palindrome
assert is_palindrome("x")  # single character
assert is_palindrome("racecar")
assert not is_palindrome("hello")

# Mixed case and punctuation (common expected behavior: ignore non-alphanumeric, case-insensitive)
assert is_palindrome("A man, a plan, a canal: Panama")
assert is_palindrome("No 'x' in Nixon")

# Numeric cases
assert is_palindrome("12321")
assert not is_palindrome("12345")

# Whitespace-only (typically treated like empty / ignored)
assert is_palindrome("   ")

# Long strings
long_pal = "a" * 200001  # odd-length long palindrome
assert is_palindrome(long_pal)

long_non_pal = "a" * 200000 + "b"  # long non-palindrome
assert not is_palindrome(long_non_pal)

print("All tests passed.")