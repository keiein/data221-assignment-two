#assignment_question_one.py
import string

text_file = open("sample-file.txt", 'r')
tokens = text_file.read().split()

tokens = [token.lower().strip(string.punctuation) for token in tokens] # iterate through the list of tokens, make it lower case, strip punctuation
tokens = [token for token in tokens if len(token) >= 2] # iterate through tokens, keep the ones that have at least 2 characters
# list comprehension

word_count_dictionary = {}

for token in tokens:
    count = tokens.count(token)
    word_count_dictionary[token] = count

flipped_word_count_dictionary = [(value, key) for key, value in word_count_dictionary.items()]
sorted_word_count_dictionary = sorted(flipped_word_count_dictionary, reverse=True)
top_five_words = sorted_word_count_dictionary[:5]

print(f"Cleaned list: {tokens}")
print(word_count_dictionary)

for element in top_five_words:
    print(f"{element[1]} -> {element[0]}")
