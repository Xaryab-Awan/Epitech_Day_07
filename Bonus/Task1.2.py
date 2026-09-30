def is_palindrome(word):
    word = word.lower()
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("Kayak"))     
print(is_palindrome("hangman"))   