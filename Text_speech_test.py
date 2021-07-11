import gtts # google text to speech, requires internet connection
import os

from playsound import playsound # method to play the audio file


def text_speech(speech):
    speech_file = gtts.gTTS(speech) # passing text ot gTTS object 
    speech_file.save("hello.mp3") # saving the retrieved audio speech from the API into a file in the current directory

    playsound("hello.mp3") # plays the audio file

    os.remove("hello.mp3")
    

a = input("Hello:")
b = f"""Hello {a}! How are you doing today"""

text_speech(b)