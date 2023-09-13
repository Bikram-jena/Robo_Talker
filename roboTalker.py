# import os
#
#
# if __name__ == '__main__':
#     print("Welcome to RoboSppeaker")
#     x = input("Enter what you want me to speak: ")
#     command = f"say {x}"
#     os.system("command")

import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            engine.say("The Robo is offline now")
            engine.runAndWait()
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
