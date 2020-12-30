@Author Rupesh

# Importing packages
from gtts import gTTS
import os

#Reading the text
Readmytext = open("Greetings.txt", "r")
Text = fh.read().replace("\n", " ")

Language ='en'

output = gTTS(text=Readmytext, lang = Language, slow=False)

#Saving output
output.save("Happy New Year 2021.mp3")

Readmytext.close()

#Playing output
os.system("start Happy New Year 2021.mp3")
