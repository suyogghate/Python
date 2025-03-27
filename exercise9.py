import win32com.client
import time

# List of names
l = ["Rahul", "Nishant", "Harry"]

# Initialize the Speech API
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Loop through the list and speak
for name in l:
    sentence = f"Shoutout to {name}"
    print(sentence)
    speaker.Speak(sentence)
    time.sleep(0.5)  # Small pause between shoutouts

print("✅ All names pronounced successfully!")


# import sys
# print(sys.path)

# import win32com.client
# print("win32com is working!")

'''
paste this line in the terminal then run
python -c "import win32com.client; s=win32com.client.Dispatch('SAPI.SpVoice'); s.Speak('Shoutout to Rahul, Nishant and Harry')"
'''