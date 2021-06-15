# Import the required module for text
# to speech conversion
from gtts import gTTS
import sounddevice as sd
from playsound import playsound
import playsound



# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Welcome to bongprogramiz! বৃষ্টি শেষে মাটির গন্ধে,ভরে উঠে মন জাগে নতুন স্বপ্ন; তাকে ছুঁবো চল। পাই নি তোমায়,ব্যাথা আছে প্রানে আমার পাশে?'

# Language in which you want to convert
language = 'bn'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
#os.system("mpg321 welcome.mp3")
playsound.playsound('welcome.mp3')

