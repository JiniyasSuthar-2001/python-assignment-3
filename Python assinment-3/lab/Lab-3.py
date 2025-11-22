#Write a Python program to open a file in write mode, write some text, and then close it


# Open a file named "example.txt" in write mode
file = open("example.txt", "w")

# Write text to the file
file.write("Hello, this is a sample text written to the file.\n")
file.write("This is the second line of text.")

# Close the file to save changes
file.close()

print("Text written to example.txt successfully.")
