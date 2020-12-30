from gtts import gTTS
import os

fh = open("Greetings.txt", "r")
Text = fh.read().replace("\n", " ")

Language ='en'

output = gTTS(text=Text, lang = Language, slow=False)

output.save("Happy New Year 2021.mp3")

fh.close()

os.system("start Happy New Year 2021.mp3")