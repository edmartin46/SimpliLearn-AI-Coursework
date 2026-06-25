def is_palindrome(text: str) -> bool:
    s = ''.join(ch.lower() for ch in text if ch.isalnum())
    return s == s[::-1]