import os
from gtts import gTTS

tts = gTTS('Olá mundo!', lang='pt-br')
tts.save('audio.mp3')
os.system("mpg123 audio.mp3") 

