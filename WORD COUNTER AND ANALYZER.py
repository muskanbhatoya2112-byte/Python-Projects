para = input("Enter a paragraph: ")

words = para.split()

# Count words
count = len(words)

# Find longest word
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

# Count vowels
vowels = 0
for ch in para.lower():
    if ch in "aeiou":
        vowels += 1

print("Number of words =", count)
print("Longest word =", longest)
print("Number of vowels =", vowels)