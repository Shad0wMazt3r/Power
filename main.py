import random
import os
import time
import re
from random_word import RandomWords

def setup():
    os.system("mkdir power_files")
    os.chdir("power_files")
    os.system("mkdir data")
    os.chdir("data")
    name = input("Please enter your name:")
    name_setup = "echo "+name+"> name"
    os.system(name_setup)
    age = input("Please enter your age:")
    age_setup = "echo "+age+"> age"
    os.system("mkdir happy_stories")
    os.system("mkdir sad_stories")
    os.system(age_setup)
    os.chdir("../..")
    print('''The set up has been completed but you may need to install the following packages:
        1. mpv (sudo apt install mpv)''')

def getName():
    os.chdir("power_files/data")
    with open('name','r') as name_file:
        name = name_file.read().replace("\n","") 
    os.chdir("../..")
    return name

def checkFeeling(user_input):
    user_input_split = user_input.split(" ")

    if "i feel " in user_input:
        if any(x in user_input_split for x in negative_feelings):
            print('Do you think you know why you have this emotion?')
            print("Negative Emotions are not good for your mental health")
            print(f"Please tell me if you know why you are feeling like this...")
            name = getName()
            user_input = input(f"\n{name}:\n>")
            user_input_split = user_input.split(" ")
            if  any(x in user_input_split for x in negation_words):
                print("Okay, But I am here for you. I will be available to listen to you anytime you wish!")
            if any(x in user_input_split for x in affirmation_words):
                print("Power:\n>I am here for you. Tell me whatever you want and I wont tell anyone")
                sad_story = input(f"{name}:\n>")
                random_name = RandomWords()
                sad_story_name = random_name.get_random_word()
                sad_story_name = sad_story_name.replace(" ","_")
                sad_story_path = "power_files/data/sad_stories/"
                os.chdir(sad_story_path)
                sad_story_file = open(sad_story_name,"w+")
                sad_story_file.write(sad_story)
                sad_story_file.close()
                os.chdir("../../../")
                print(f"Power:\n>I have noted down your story, {name}! I remember it as {sad_story_name}")
        elif any(x in user_input_split for x in positive_feelings):
            print("I am glad you feel that way! Would you like to tell me why you feel that way?")
            name = getName()
            user_input = input(f"\n{name}:\n>")
            user_input_split = user_input.split(" ")
            if  any(x in user_input_split for x in negation_words):
                print("Okay, Keep up the positive emotions!")
            if any(x in user_input_split for x in affirmation_words):
                print("Power: \n>I am excited to hear your story!")
                happy_story = input(f"{name}: \n>")
                random_name = RandomWords()
                happy_story_name = random_name.get_random_word()
                happy_story_name = happy_story_name.replace(" ","_")
                happy_story_path = "power_files/data/happy_stories/"
                os.chdir(happy_story_path)
                happy_story_file = open(happy_story_name,"w+")
                happy_story_file.write(happy_story)
                happy_story_file.close()
                os.chdir("../../../")
                print(f"Power: \n>I have noted down your story, {name}! I remember it as {happy_story_name}")
    if "i am " in user_input: 
        if  any(x in user_input_split for x in negative_feelings):
            print("Do you know why you feel that way?")
            print("Negative feelings are inevitable but they do not define you")
            print(f"Please tell me if you know why you are feeling like this...")
            name = getName()
            user_input = input(f"\n{name}:\n>")
            user_input_split = user_input.split(" ")
            if  any(x in user_input_split for x in negation_words):
                print("Okay, But I am here for you. I will be available to listen to you anytime you wish!")
            if any(x in user_input_split for x in affirmation_words):
                print("Power:\n>I am here for you. Tell me whatever you want and I wont tell anyone")
                sad_story = input(f"{name}:\n>")
                random_name = RandomWords()
                sad_story_name = random_name.get_random_word()
                sad_story_name = sad_story_name.replace(" ","_")
                sad_story_path = "power_files/data/sad_stories/"
                os.chdir(sad_story_path)
                sad_story_file = open(sad_story_name,"w+")
                sad_story_file.write(sad_story)
                sad_story_file.close()
                os.chdir("../../../")
                print(f"Power:\n>I have noted down your story, {name}! I remember it as {sad_story_name}")
        else:
            if  user_input.startswith("i am "):
                name = user_input.replace("i am ", "")
                print(f"Hi, {name}, Would you like me to change your name?(y/n):", end='')
                name_change_req = input("")
                name_change_req = name_change_req.lower()

                if name_change_req == "y" :
                    name_setup = "echo "+name+"> power_files/data/name"
                    print("Your name has changed")

    elif "song" in user_input_split:
        if "listen" in user_input_split:
            print(f"Power:\n>Playing you a song right away!\n")
            song_list = ['https://www.youtube.com/watch?v=xo1VInw-SKc','https://www.youtube.com/watch?v=bMpFmHSgC4Q','https://www.youtube.com/watch?v=Dkk9gvTmCXY','https://www.youtube.com/watch?v=6BYIKEH0RCQ','https://www.youtube.com/watch?v=v2-9rIL_f4w','https://www.youtube.com/watch?v=zaCbuB3w0kg','https://www.youtube.com/watch?v=7tNPxY_ntEA']
            random_song_no = random.randint(0,6)
            random_song_link = song_list[random_song_no]
            play_random_song = 'mpv '+random_song_link
            os.system(play_random_song)
def getResponse(user_input):
    user_input = user_input.lower()
    user_input_split = user_input.split(" ")
    if len(user_input_split) < 3:
        if any(x in user_input_split for x in first_greeting):
            print(random_first_greeting)
        else:
            checkFeeling(user_input)
    else:
        checkFeeling(user_input)

if os.path.exists('power_files/data'):
    pass
else:
    print("Setting up Power for first time use...")
    print("Don't worry this will take place only once")
    setup()

first_greeting = ["Hi","Hello", "Hey","Hola", "Konnichiwa", "Namaste"]

greeting = ["How are you?","How’s it going?","How ya doin’?","How are things?","How’s life?","How have you been?","What’s up?","What’s new?","What have you been up to lately?"]

first_random_number = random.randint(0,5)
random_first_greeting = first_greeting[first_random_number]

random_number = random.randint(0, 8)
random_greeting = greeting[random_number]

name = getName()

print("Power:")
print(">"+random_first_greeting, name+", "+random_greeting)
print("I am Power, I am your friend!, Do not hesitate to talk to me.")

first_greeting = ["hi","hello", "hey","hola", "konnichiwa", "namaste"]

negative_feelings = ['sad','depressed','tired','restless','lonely','jealous','fear','afraid','angry','anger','hate', 'disgust', "awful"]

positive_feelings = ['happy','excited','joyful','awesome','interested','hopeful','prideful','amused', 'inspired', 'motivated', 'grateful', 'lovely', "cool","amazing"]

negation_words = ['no', 'nah', 'not', 'nay','nope', 'none', 'nobody', 'nothing', 'nowhere', 'never', "shouldn't", "won't", "can't", "don't", "shouldnt","wont", "cant","dont"]

affirmation_words = ['yes',"ya", 'yeah', 'yup', 'ok','alright', "all right", "sure", "certainly", "absolutely", "indeed","aye", "of course", "ofcourse", "ofc","yep", "yah","okay","surely", "yea"]

while True:
    user_input = input(f"\n{name}:\n>")
    print("\nPower:\n>", end='')
    getResponse(user_input)

