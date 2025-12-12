from gtts import gTTS
import os

say = "Hello my name is Amartya"
language = 'en'

speech = gTTS(text = say, lang= language, slow = False)
speech.save("speecch.mp3")
os.system("start speecch.mp3")
