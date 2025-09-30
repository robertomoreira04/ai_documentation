import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")

phrase = input("Digite uma frase para ouvir o áudio")
engine.say(phrase)
engine.runAndWait()