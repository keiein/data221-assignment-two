#assignment_question_three.py
import string

text_file = open("sample-file.txt", 'r') #open file

cleaned_lines = [] #list for cleaned lines
original_lines = [] #list for the original lines
for line in text_file:
    original_lines.append(line.strip()) #add to the list of original lines, without the leading, trailing whitespace
    words=line.split() #words into list
    words = [word.strip(string.punctuation).lower() for word in words] #list comprehension for stripping punct, to lowercase
    words = [word for word in words if len(word) >= 2] #only keep the words with more than 2 characters
    cleaned_lines.append("".join(words)) #join the words together without any spaces

repeated_dictionary = {} #used for counting

for i in range(len(cleaned_lines)): #iterate through, count, then if it shows up more than once then put into dictionary
    count = cleaned_lines.count(cleaned_lines[i])
    if count > 1 and len(cleaned_lines[i])>0:
        if cleaned_lines[i] in repeated_dictionary:
            repeated_dictionary[cleaned_lines[i]].append(i+1)
        else:
            repeated_dictionary[cleaned_lines[i]] = [i+1]


print(f"Number of sets: {len(repeated_dictionary)}") #counts the number of keys
first_two_count = 0 #used so that only the first two will be printed

for key, value in repeated_dictionary.items():
    if first_two_count < 2:
        first_two_count += 1
        for line_num in value:
            print(f"{line_num}. {original_lines[line_num-1]}")

