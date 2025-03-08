import os

for i in range(1, 101):
    os.rename(f"data/Tutorial{i}", f"data/Tutorial {i}")