#Write a Python program to match a word in a string using re.match().


import re

# Sample text
text = "Python is a powerful programming language."

# Word to match at the beginning
word = "Python"

# Use re.match() to check if the text starts with the word
match = re.match(word, text)

if match:
    print(f"The text starts with '{word}'.")
else:
    print(f"The text does not start with '{word}'.")
