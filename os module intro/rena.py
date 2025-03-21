'''
Write a program to clear the clutter inside a folder on your computer. 
You should use os module to rename all the png images from 1.png all the way till n.png 
where n is the number of png files in that folder. Do the same for other file formats. For example:

sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png
'''
import os

# for i in range(1, 101):
#     os.rename(f"data/Tutorial{i}", f"data/Tutorial {i}")

# files = os.listdir("data2")
files = os.listdir(r"E:\Python\os module intro\data2")

i = 1
for file in files:
  if file.endswith(".jpg"):
    print(file)
    os.rename(f"E:\Python\os module intro\data2/{file}", f"E:\Python\os module intro\data2/{i}.jpg")
    i = i + 1