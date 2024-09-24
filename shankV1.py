import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id) #keep it as 0 to get a male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("I am shank, nice to meet you")
    speak("Tell me what to do")


def takeCommand():
    #listens to your command and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again")
        return "none"
    return query

def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('my@gmail.com', 'your-password')
    server.sendmail('my@gmail.com',to, content )
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() 

        #logic for task execution based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir= "C:\\Users\\USER\\Desktop\\projects\\virtual assistance" #put songs
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\SHASHANK\\just shank\\Microsoft VS Code\\Code.exe" #put proper path
            os.startfile(codePath)

        elif 'email to shashank' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "to@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry shashank, not able to send the email ")            
        #to be able to send a mail, you need to enable less secured apps in your gmail account

        elif 'close' in query:
            break
        else:
            pass