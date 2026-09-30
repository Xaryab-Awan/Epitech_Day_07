def frequency(word):
    counts = {}
    for ch in word:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def most_frequent(word):
    counts = frequency(word)
    best = max(counts.values())
    return min(ch for ch, n in counts.items() if n == best)

print(frequency("banana"))      
print(most_frequent("banana"))  
print(most_frequent("abab"))   