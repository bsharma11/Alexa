import speech_recognition as sr
import pyttsx3  # package python text to speech
import pywhatkit as kit
import datetime as dt
import wikipedia as wiki
import pyjokes as jokes
#install all the above packages as well as pyaudio

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.say("This is google, how may i help you")
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def processing():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'google' in command:
                command = command.replace('google', "")
            return command
    except:
        pass


def run():
    p = 0
    while p != 1:
        words = processing()
        if words == None:
            talk("Sorry can you please speak again")
        elif 'play' in words:
            words = words.replace('play', '')
            talk("Playing" + words)
            kit.playonyt(words)
            break
        elif 'time' in words:
            time = dt.datetime.now().strftime('%I:%M %p')
            # strftime refers to string format of time,
            ## %H refers to 24h format og time and %I refers to 12h format,%p tells am/pm
            print(time)
            talk('Current time is' + time)
            break
        elif 'who is' in words:
            words = words.replace('who is ', "")
            info = wiki.summary(words, 2)
            print(info)
            talk(info)
            break
        elif 'joke' in words:
            talk(jokes.get_jokes())
            break
        else:
            talk("Sorry didn't get you")
            talk("To talk to me run the code")
            p += 1


run()
