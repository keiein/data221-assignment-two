#assignment_question_two.py
import string

text_file = open("sample-file.txt", 'r')
tokens = text_file.read().split()

tokens = [token.lower().strip(string.punctuation) for token in tokens] # iterate through the list of tokens, make it lower case, strip punctuation
tokens = [token for token in tokens if len(token) >= 2] # iterate through tokens, keep the ones that have at least 2 characters
bigrams = [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]
# list comprehension

bigram_dictionary = {}
for bigram in bigrams:
    count = bigrams.count(bigram)
    if count > 1:
        bigram_dictionary[bigram] = count

#sorting
flipped_bigrams = [(value, key) for (key, value) in bigram_dictionary.items()]
flipped_bigrams_sorted = sorted(flipped_bigrams, reverse=True)
reverted_bigrams = [(key, value) for (value, key) in flipped_bigrams_sorted]
top_five_words = reverted_bigrams[:5]



print(f"Cleaned list: {tokens}")

for element in top_five_words:
    print(f"{element[0][0]} {element[0][1]} -> {element[1]}")