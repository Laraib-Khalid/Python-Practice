import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

names = ["Amyma Usman","Abu Bakar Arshad", "Omar Baig", "Laraib Khalid", "Ahmad Raza"]

for name in names:
    text = f"Shoutout to {name}! You're amazing!"
    print(text)
    speaker.Speak(text)
