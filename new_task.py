user_name = input("Please enter your name: ")

num_characters = len(user_name)

print(num_characters)
# to store frequency of characters
char_frequency = {}

for char in user_name:
  if char in char_frequency:
    char_frequency[char] += 1
    else:
        char_frequency[char] = 1
num_duplicates = sum(1 for freq in char_frequency.values() if freq > 1)
print("Total number of duplicate characters:", num_duplicates)

split_words = user_name.split()

count_of_words = len(split_words)

print("the total number of words after splitting:",count_of_words)

words = user_name.lower().split()
word_frequency = {}

for word in words:
  if word.isalpha():
    word_frequency[word] = word_frequency.get(word, 0) + 1
num_duplicate_words = sum(1 for freq in word_frequency.values() if freq > 1)
print(num_duplicate_words)

reversed_characters = user_name[::-1]
print(reversed_characters)

reverse_words = user_name.split()
reversed_words = ' '.join(reverse_words[::-1])
print("Reversed words:", reversed_words)







