def is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())

print(is_anagram("listen", "silent"))   
print(is_anagram("hello", "world"))   