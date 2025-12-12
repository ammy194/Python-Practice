from gtts import gTTS
import os

say = "Hello!!! my name is Amartya. Do you want me to cook maggie"

language = 'en'

speech = gTTS(text=say, lang=language, slow=False)

speech.save("speech.mp3")

os.system("start speech.mp3")  

