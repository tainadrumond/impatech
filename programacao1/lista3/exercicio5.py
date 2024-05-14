def isAnagram(text1: str, text2: str):
    sorted_text1 = ''.join(sorted(text1))
    sorted_text2 = ''.join(sorted(text2))
    print(sorted_text1, sorted_text2)
    return sorted_text1 == sorted_text2

print(isAnagram('aabbcc', 'abcabc'))