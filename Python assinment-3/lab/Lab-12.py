#Write a Python program to search for a word in a string using re.search()

import re

# Sample text
text = "Hello, welcome to the world of Python programming."

# Word to search
word = "Python"

# Use re.search() to find the word in the text
match = re.search(word, text)

if match:
    print(f"'{word}' found in the text!")
else:
    print(f"'{word}' not found in the text.")
