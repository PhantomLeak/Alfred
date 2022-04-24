import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile('audio_files_harvard (2).wav')
with harvard as source:
    audio = r.record(source)

r.recognize_google(audio)