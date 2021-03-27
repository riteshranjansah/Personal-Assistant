import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import smtplib
import random
import time
import pyautogui as pg

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak ("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak ("I am Jarvis speed 1 gigabyte memory 1 tegabyte, please tell me how may i help you") 

def takeCommand():
#it take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    
    except Exception as e:
        #print(e)
        
        print("Say that again")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('riteshranjansaroj@gmail.com','password')
    server.sendmail('riteshranjansaroj@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace('Wikipedia',"")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'bye' in query:
            speak("Thank you sir, Have a Good day ")
            quit()

        elif query=='nothing':
            speak("ok sir, Have a Good day ")
            quit()

        elif 'thank you' in query:
            speak("Thank you sir, Have a Good day ")
            quit()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            quit()

        elif 'open google' in query:
            webbrowser.open("google.com")
            quit()

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            quit()

        elif 'play music' in query:
            music_dir = 'C:\\Users\\rites\\Videos\\Songs'
            song = os.listdir(music_dir)
            #print(song)
            os.startfile(os.path.join(music_dir, song[int(random.randint(0,len(music_dir)))]))
            quit()
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'email to' in query:
            try:
                speak("What you want to say ?")
                content = takeCommand()
                to = "someone_email@gmail.com"
                sendEmail(to, content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("Sorry sir, Can't able to send email at this moment")
