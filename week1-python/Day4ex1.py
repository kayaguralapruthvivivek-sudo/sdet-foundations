def is_palindrome(word):
    word = word.lower()
    length = len(word)

    for i in range(0, length//2):
        if word[i] != word[length-1-i]:
            return False
    return True    

result = is_palindrome("NrtiN")
print(result)