#Write a Python program to write multiple strings into a file.

# Strings to write to the file
lines = [
    "This is the first line.\n",
    "Here is the second line.\n",
    "And this is the third line.\n"
]

# Open the file "multilines.txt" in write mode
with open("multilines.txt", "w") as file:
    # Write each string from the list to the file
    for line in lines:
        file.write(line)

print("Multiple strings have been written to multilines.txt successfully.")
