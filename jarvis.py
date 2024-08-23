import pyttsx3 as p
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import shutil
import smtplib





engine= p.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("what are you doing")
def wishme():
    hour=  int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
        speak("i am jarvis please tell me hoe i can help you") 
    elif hour>12 & hour<18:
        speak('Good afternoon')
        speak("i am jarvis so please tell me how i can help you")
        

    else:
        speak('good night')  
        speak("i am jarvis please tell me how i can help you")  
wishme()
def takecommand():
    '''
    it take microphone input from the user and returns string object
    '''
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold= 1
        audio= r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said// {query}")
        return query 
    except:
        print("say again please...")


        
while 1: 
    a=takecommand().lower()
    
    
    if 'wikipedia' in a:
        speak('Searching wikipedia...')
        a= a.replace("wikipedia","")
        result= wikipedia.summary(a,sentences=10)
        speak(result)
        print(result)
        break
    elif 'youtube' in a:
        webbrowser.open('youtube.com')
        break
    elif ' google' in a:
        webbrowser.open("google.com")
        break
    elif 'whatsapp' in a:
        speak("your result is ready")
        webbrowser.open("whatsapp.com")
        break
    elif "birthday photo" in a:
        os.startfile(r"C:\Users\BIT\OneDrive\Pictures")
        break
    elif 'time' in a:
        st= datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir the time is {st}")
        break
    elif "file" in a:
        shutil.copy('result.png','new image.jpg')
        speak("created your file")
        print("succesfully created...")
        break
    elif "code" in a:
        os.startfile(r"C:\Users\BIT\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    
        
        






















       

#logic for executing tasks based on query
 
















 

























    

            














