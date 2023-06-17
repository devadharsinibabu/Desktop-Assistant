
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Iam Jarvis")
    speak("what should i call you my dear friend")
    uname=takeCommand()
    speak("Welcome Miss")
    speak(uname)
    speak("How can i help you?")


def takeCommand():
    #It takes microphone input from the user and returns string output
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
       # print(e)

        print("Say that again please...")
        return "None"
    return query
    

if __name__== "__main__":
    wishMe()
   # while True:
    if 1:

        query = takeCommand().lower()
        #logic for executing tasks basd on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(f'{query}',sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open flipkart' in query:
            webbrowser.open("open flipkart.com")

        elif 'what is the time' in query:  
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            speak(f"The time is {strTime} ")

        elif 'open code' in query:
            codePath="C:\\Users\\Deva\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(codePath)

            
        elif 'shutdown the system' in query:
            speak("Hold On a sec! Your system is shuting down")
            os.system("shutdown /s /t 1")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
       
           
        
            