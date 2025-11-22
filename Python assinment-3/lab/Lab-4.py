#Write a Python program to read the contents of a file and print them on the console

# Open the file named "example.txt" in read mode
with open("example.txt", "r") as file:
    # Read all content from the file
    content = file.read()

# Print the content on the console
print("Contents of the file:")
print(content)
