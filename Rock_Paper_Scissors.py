import random # for the random integer generator
import gtts # to translate text to speech
from io import BytesIO # create a temporary folder to hold the audio files
import os # to use the OS structure commands
from playsound import playsound # to play the output sound


# global variables
# dictionary to convert the random integer to either rock, paper or scissors
choices_dict_int = {
    0 : "rock",
    1 : "paper",
    2 : "scissors"
}

# dictionary to convert the input string to either 0, 1 or 2
choices_dict_str = {
    "rock" : 0,
    "paper" : 1,
    "scissors" : 2
}

# get the random integer 
def random_probability():
    return random.randint(0, 2)

# text to speech
def text_speech(speech):
    speech_file = gtts.gTTS(speech)
    speech_file.save("audio_file.mp3")

    playsound("audio_file.mp3")

    os.remove("audio_file.mp3")

# funciton to check who wins, gives a return value of result and speech text
def check_win_who(user_ch, chances_int):
    if choices_dict_str[user_ch.lower()] == chances_int: # draw case
        print(f"You showed {user_ch.lower()} and the computer showed {choices_dict_int[chances_int]}. Its a draw!")
        result = "draw"
        # text to speech code
        speech = f"You showed {user_ch.lower()} and the computer showed {choices_dict_int[chances_int]}. Its a draw!"

    elif choices_dict_str[user_ch.lower()] == 0 and chances_int == 1: # losing case no. 1: user = rock, comp = paper
        print(f"You showed {user_ch.lower()} and the computer showed {choices_dict_int[chances_int]}. Computer Wins!")
        result = "computer wins"
        # text to speech code
        speech = f"You showed {user_ch.lower()} and the computer showed {choices_dict_int[chances_int]}. Computer Wins!"

    elif choices_dict_str[user_ch.lower()] == 1 and chances_int == 2: # losing case no. 2: user = paper, comp = scissors
        print(f"You showed {user_ch.lower()} and the computer showed {choices_dict_int[chances_int]}. Computer Wins!")
        result = "computer wins"
        # text to speech code
        speech = f"You showed {user_ch.lower()} and the computer showed {choices_dict_int[chances_int]}. Computer Wins!"

    elif choices_dict_str[user_ch.lower()] == 2 and chances_int == 0: # losing case no. 3: user = scissors, comp = rock
        print(f"You showed {user_ch.lower()} and the computer showed {choices_dict_int[chances_int]}. Computer Wins!")
        result = "computer wins"
        # text to speech code
        speech = f"You showed {user_ch.lower()} and the computer showed {choices_dict_int[chances_int]}. Computer Wins!"

    else: # user winning case
        print(f"You showed {user_ch.lower()} and the computer showed {choices_dict_int[chances_int]}. You Win!")
        result = "user wins"
        # text to speech code
        speech = f"You showed {user_ch.lower()} annd the computer showed {choices_dict_int[chances_int]}. You Win!"

    return result, speech

# rock, paper and scissors function
def rps_fn(chances_int):
    # variable initialization
    user_win = 0
    comp_win = 0
    draw = 0
    result_who = ""

    # flags initialization
    cont = ""
    flag = True
    
    while flag:
        text_speech("Please enter either rock, paper or scissors: ") # text to speech of input prompt
        user_sign = input("Please enter either rock, paper or scissors: ") # input prompt
        
        # test to check if the user has input a valid option
        while user_sign.lower() != "rock" and user_sign.lower() and "paper" and user_sign.lower() != "scissors":
            print("Please input a valid option of either rock paper or scissors")
            text_speech("Please input a valid option of either rock paper or scissors")
            user_sign = input(">")

        # return value from the check_win_who function
        return_value = check_win_who(user_sign, chances_int)
        speech = return_value[1] # text to speech part
        result_who = return_value[0] # who wins part

        if result_who == "computer wins":
            comp_win += 1
        elif result_who == "user wins":
            user_win += 1
        else:
            draw += 1

        # text to speech function call
        text_speech(speech)

        speech = "Would you like to continue?"
        text_speech(speech)

        cont = input("Would you like to continue? (Y/N): ")
        print("\n")

        # text to speech function call
        text_speech("Thank you for confirming!")

        # needs working, if y or n then go ahead else repeat this "Please enter a valid key (Y/N): "
        chances_int = random_probability()

        while cont.lower() != "y" and cont.lower() != "n":
            print("Please enter a valid keyword of either 'y' or 'n': ")
            text_speech("Please enter a valid keyword of either 'y' or 'n': ")
            cont = input(">")
        else:
            if cont.lower() == "n":
                flag = False
            
    return (user_win, comp_win, draw)

# driver code
if __name__ == "__main__":
    result = rps_fn(random_probability())

    # output prompt along with the scoreboard        
    print(f"""Thank you for playing this game! \n
            The total scoreboard for this game is:\n
            User wins: {result[0]}\n
            Computer wins: {result[1]}\n
            Number of draws: {result[2]}""")







