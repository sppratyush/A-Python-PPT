s = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
v = sum(1 for ch in s if ch in vowels)
c = sum(1 for ch in s if ch.isalpha() and ch not in vowels)

print("Vowels:", v)
print("Consonants:", c)
print("Reversed:", s[::-1])
print("Underscore:", s.replace(" ", "_"))
print("Capitalized:", s.title())