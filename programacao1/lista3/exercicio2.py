def isPalindrome(text: str):
    str_length = len(text)
    for i in range(str_length//2):
        if (text[i] != text[str_length-i-1]):
            return False
    return True

print(isPalindrome('subinoonibus'))