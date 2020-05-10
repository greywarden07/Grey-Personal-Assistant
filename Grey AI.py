import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am Grey an Ai assistant!. Please tell me how can I help you sir ?")       

def takeCommand():
    

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        
        print("Listening...")
       
        audio = r.listen(source)

    try:
        
        print("Recognizing...")    
        
        query = r.recognize_google(audio, language='en-in')
        
        print(f"User said: {query}\n")

    except Exception as e:
          
        
        print("Say that again please...")  
        
        return "None"
    
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("Have a great day sir!")
            break

        
        
        
        
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/")
            speak("Have a great day sir!")
            break

        

        
        
        
        
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("https://open.spotify.com/?_ga=2.141017650.1862246344.1588341203-784159556.1587555129")

            speak("Have a great day sir!")
            break   

        
        
        
        
        
        elif 'open chrome' in query:
            speak("opening chrome")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chromepath)
            speak("Have a great day sir!")
            break
        
        
        
        
        
        
        elif 'time please' in query:
            speak("your time is always good sir and")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            speak("Have a great day sir!")
            break

        
        
        
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("https://github.com/")
            speak("Have a great day sir!")
            break
           
        
        
        
        
        
        elif 'open gitlab' in query:
            speak("opening gitlab")
            webbrowser.open("https://lab.inversion.co.in/users/sign_in")
            speak("Have a great day sir!")
            break
            
        
        
        
        
        elif 'open gmail' in query:
            speak("opening gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/#")
            speak("Have a great sir!")
            break

        
        
        
        
        elif 'quit' in query:
            speak("Have a great day sir!")
            break
        
        
        
        
        
        elif 'hello grey' in query:
            speak("Hello sir. What can I help you ?")
            continue
        
        
        elif 'open medibang' in query:
            speak("opening medibang")
            medipath = "C:\Program Files\Medibang\MediBang Paint Pro\MediBangPaintPro.exe"
        
            os.startfile(medipath)
            speak("Have a great day sir!")
            break
        
       
        
        
        else:
            speak("Have a great day sir!")
            break
        

