import PYTTSX3 as speaker
tts = speaker.init()

def say(text):
   tts.say(text)
   tts.runAndWait()

a = "Hello Boss I am your program"
say(a)