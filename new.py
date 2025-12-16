import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

def talk(text):
    print("alexa:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    #listen to user voice and recognize the command
    command = ""
    try:
        with sr.Microphone() as source:
            print("listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print("User:", command)
    except sr.UnknownValueError:
        print("Sorry, I did not get that.")
    except sr.RequestError:
        print("network error.Check your internet connection.")
    return command

def run_alexa():
    #process the command and respond accordingly
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk("playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I : %M :%p')
        talk("The current time is " + time)

    elif 'who is' in command or 'who the heck is' in command:
        person = command.replace('who the heck is', '').replace('who is', '').strip()
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    elif 'date' in command:
        talk("sorry. I have a headache today.")

    elif 'are you single' in command:
        talk("i am in a relation with wi-fi.")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif command != "":
        talk("please say the command again.")
    else:
        pass #no voice detected. Ignore quietly

    
while True: ## run Alexa continuously
    run_alexa()