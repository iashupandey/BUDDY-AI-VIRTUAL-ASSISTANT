import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import random
import webbrowser
import os
import smtplib
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")

    speak("all systems are getting ready")
    speak("all set Now...")
    speak("Tell me how can i help you")
    
def takecomand():
    #it takes my microphone input from user and returns string output

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.energy_threshold = 500
        r.pause_threshold = 1
        audio = r.listen(source)           

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None" 
    return query                                 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourgmail788@gmail.com', 'password12')   #enter your gmail and password
    server.sendmail('sendergmail@gmail.com', to, content)  #enter your gmail
    server.close()
    

if __name__ == "__main__":
    print("***************************************************************************************************")
    wishMe()
    speak("I am your BUDDY, here to present myself as your reliable buddy")
    while True:
        query = takecomand().lower()

        #logic for excuting tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query= query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('Alright!!')
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube...")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("what should I search on google")
            cm = takecomand().lower()
            if 'just open it' in cm:
                speak("opening google...")
                webbrowser.open("https://google.com/")
            elif '' in cm:
                speak("searching...")
                webbrowser.open('https://google.com/?#q=' + cm)


        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            #print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        
        elif 'open code' in query:
            codePath = "C:\\Users\\nikhi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #this is the path of my laptop change it with your laptop path
            os.startfile(codePath)

        elif 'open notepad' in query:
            notePath = "C:\\Windows\\system32\\notepad.exe"             #this is the path of my laptop change it with your laptop path
            os.startfile(notePath)

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'send email' in query:
            try:
                speak("what should I say")
                content = takecomand()
                to = "nirbhaynirpur05@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry my sir but i'm unable  to send this email")

        elif 'who are you' in query:
            speak("i am no one but you can recognige me as BUDDY")

        elif 'what can you do for me' in query:
            speak("I can answer your queries and perform different tasks for you like searching, sending mails, runnning applications and many more")

        elif 'whats my ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif 'how are you' in query:
            speak("I am well, how can I help you")

    
        elif 'ok sir quit' in query:
            speak("thank you for operating me Sir")
            print(" _$$$$$$___$$$$$$_ ")
            print("_$$$$$$$$_$$$$$$$$_  ")
            print("_$$$$$$$$$$$$$$$$$_  ")
            print(" _$$$$$$$$$$$$$$$_   ")
            print(" ___$$$$$$$$$$$___   ")
            print(" _____$$$$$$$_____   ")
            print(" _______$$$_______   ")
            print(" ________$________ ")
            exit()