from gtts import gTTS
import pygame

text="Hello Rasa Bot User! I am a Bot"
tts = gTTS(text=text, lang="en")
tts.save("temp.mp3") # save the audio in a temp file 
pygame.mixer.init()

pygame.mixer.music.load('temp.mp3')
pygame.mixer.music.play()


#pygame.mixer.music.load('temp.mp3')# load the audio file
#pygame.mixer.music.play()