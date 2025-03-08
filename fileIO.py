# Reading from a file
# f = open('myfile.txt', 'r')
# contents = f.read()
# print(contents)

# Writing into a file
# f = open('myfile.txt', 'w')
# f.write('Hello, world!')
# Keep in mind that writing to a file will overwrite its contents. 
# If you want to append to a file instead of overwriting it, you can 
# open it in append mode.
# f = open('myfile.txt', 'a')
# f.write('Code With Harry ')

# It is important to close a file after you are done with it. 
# This releases the resources used by the file and allows other 
# programs to access it.

# To close a file, you can use the close() method.
# f.close()

# Alternatively, you can use the with statement to automatically 
# close the file after you are done with it.
# with open('myfile.txt', 'r') as f:
    # ... do something with the file

# read, readlines and other methods---------------------------------
# The readline() method reads a single line from the file. 
# If we want to read multiple lines, we can use a loop.

# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)


# The writelines() method in Python writes a sequence of strings to a file. 
# The sequence can be any iterable object, such as a list or a tuple.

# This will write the strings in the lines list to the file myfile.txt. The \n characters are 
# used to add newline characters to the end of each string.
# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()


# Keep in mind that the writelines() method does not add newline 
# characters between the strings in the sequence. 
# If you want to add newlines between the strings, you can use a 
# loop to write each string separately:
# f = open('myfile.txt', 'w')
# lines = ['line 1', 'line 2', 'line 3']
# for line in lines:
#     f.write(line + '\n')
# f.close()

# ----------------------------------------------------------
# f = open('myfile.txt', 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of student {i} in Maths is : {m1}")
#     print(f"Marks of student {i} in English is : {m2}")
#     print(f"Marks of student {i} in SST is : {m3}")
#     print(line)

# --------------------------------------------------------
# seek() and tell() functions
# The seek() function allows you to move the current position 
# within a file to a specific point. The position is specified 
# in bytes, and you can move either forward or backward from the current position. 
# with open('file.txt', 'r') as f:
  # Move to the 10th byte in the file
#   f.seek(10)

  # Read the next 5 bytes
#   data = f.read(5)
#   print(data)
#   f.close()

# The tell() function returns the current position within the file, in bytes. 
# This can be useful for keeping track of your location within the file or for 
# seeking to a specific position relative to the current position
# with open('file.txt', 'r') as f:
  # Read the first 10 bytes
#   data = f.read(10)

# Save the current position
#   current_position = f.tell()

# Seek to the saved position
#   f.seek(current_position)
#   print(current_position)
#   f.close()

# When you open a file in Python using the open function, you can 
# specify the mode in which you want to open the file.
# If you specify the mode as 'w' or 'a', the file is opened in write
# mode and you can write to the file. 
# However, if you want to truncate the file to a specific size, you 
# can use the truncate function.
# with open('sample.txt', 'w') as f:
#   f.write('Hello World!')
#   f.truncate(5)

# with open('sample.txt', 'r') as f:
#   print(f.read())

with open('sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(4)

with open('sample.txt', 'r') as f:
  print(f.read())