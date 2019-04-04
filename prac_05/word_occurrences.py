word_occurences = {}

string = input("Enter string")

words = string.split()

for word in words:
    count = word_occurences.get(word, 0)
    word_occurences[word] = count + 1

words = []
for key in word_occurences:
    words.append(key)
words.sort()
print(words)

max_len = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_len, word_occurences[word]))