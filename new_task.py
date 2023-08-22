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

