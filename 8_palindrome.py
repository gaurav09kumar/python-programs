#string is a palindrome
def is_palindrome(text):
    new_text = text.lower().replace(" ","")
    print(f"{text} is a palindrome") if new_text==new_text[::-1] else print(f"{text} is not a palindrome")

is_palindrome("abcba")
is_palindrome("test")
