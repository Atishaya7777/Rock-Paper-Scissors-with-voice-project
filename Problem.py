import random # for the random integer generator
import gtts # to translate text to speech
from io import BytesIO # create a temporary folder to hold the audio files
import os # to use the OS structure commands
from playsound import playsound # to play the output sound


def text_speech(speech):
    speech_file = gtts.gTTS(speech)
    speech_file.save("audio_file.mp3")

    playsound("audio_file.mp3")

    os.remove("audio_file.mp3")

user_sign = input("Please enter either rock, paper or scissors: ") # input prompt

        # test to check if the user has input a valid option
while user_sign.lower() != "rock" and user_sign.lower() and "paper" and user_sign.lower() != "scissors":
    print("Please input a valid option of either rock paper or scissors")
    text_speech("Please input a valid option of either rock paper or scissors")
    user_sign = input(">")

print(user_sign)