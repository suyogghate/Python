# import os

# # Open the file in read-only mode
# f = os.open("myfile.txt", os.O_RDONLY)

# # Read the contents of the file
# contents = os.read(f, 1024)
# print(contents)

# # Close the file
# os.close(f)

# import os

# Open the file in write-only mode
# f = os.open("myfile.txt", os.O_WRONLY)

# Write to the file
# os.write(f, b"Hello, World!")

# Close the file
# os.close(f)

# import os

# Get a list of the files in the current directory
# files = os.listdir(".")
# print(files)

# import os

# Create a new directory
# os.mkdir("newdir")

# import os

# Run the "dir" command and print the output
# output = os.system("dir")
# print(output) 

import os

# Run the "dir" command and get the output as a file-like object
f = os.popen("dir")

# Read the contents of the output
output = f.read()
print(output) 

# Close the file-like object
f.close()