# Reading a File
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Writing to a File
with open("example.txt", "w") as file:
    file.write("This is an example of writing to a file.\n")
    file.write("This will overwrite the file if it already exists.\n")

# Appending to a File
with open("example.txt", "a") as file:
    file.write("This line is added to the file without overwriting existing content.\n")

# Reading a File Line by Line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Writing a List of Lines to a File
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)
