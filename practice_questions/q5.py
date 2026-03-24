words = ["madam", "hello world", "racecar", "python"]

sorted_words = sorted(words, key=len)
print("Sorted by length:", sorted_words)

palindromes = [w for w in words if w == w[::-1]]
print("Palindromes:", palindromes)

hyphen_words = [w.replace(" ", "-") for w in words]
print("Hyphen replaced:", hyphen_words)