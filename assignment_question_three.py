#assignment_question_three.py
import string

text_file = open("sample-file.txt", 'r')

cleaned_lines = []
original_lines = []
for line in text_file:
    original_lines.append(line.strip())
    words=line.split()
    words = [word.strip(string.punctuation).lower() for word in words]
    words = [word for word in words if len(word) >= 2]
    cleaned_lines.append("".join(words))

repeated_dictionary = {}

for i in range(len(cleaned_lines)):
    count = cleaned_lines.count(cleaned_lines[i])
    if count > 1 and len(cleaned_lines[i])>0:
        if cleaned_lines[i] in repeated_dictionary:
            repeated_dictionary[cleaned_lines[i]].append(i+1)
        else:
            repeated_dictionary[cleaned_lines[i]] = [i+1]


print(f"Number of sets: {len(repeated_dictionary)}")
first_two_count = 0

for key, value in repeated_dictionary.items():
    if first_two_count < 2:
        first_two_count += 1
        for line_num in value:
            print(f"{line_num}. {original_lines[line_num-1]}")

