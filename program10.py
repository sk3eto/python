text = input("Enter a paragraph: ")

sentences = text.split(".")

sentences = [s for s in sentences if s.strip()]

words = text.split()
word_count = len(words)

if words:
	longest = max(words, key = len)
else:
	longest = ""

freq = {}

for w in words:
	w = w.lower()
	if w in freq:
		freq[w] += 1
	else:
		freq[w] = 1

print("No. of sentences: ", len(sentences))
print("No. of words: ", word_count)
print("Longest word: ", longest)
print("Word frequency: ", freq)
