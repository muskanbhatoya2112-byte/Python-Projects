text = input("Enter a passage: ")

words = text.lower().split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

top5 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]

print("Top 5 Frequent Words:")
for word, count in top5:
    print(word, ":", count)
    