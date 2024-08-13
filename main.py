'''
1: Run command - python main.py
2: say jarvis and eg open google
'''
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "13e77c1fc4bd4ab3af4044563f66468f"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open Youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=13e77c1fc4bd4ab3af4044563f66468f")
        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])

if __name__ == "__main__":
    speak("Installing jarvis......")
    while True:
        r = sr.Recognizer()
        

        print("recognizing")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if word.lower() == "jarvis" :
                speak("ya")
            with sr.Microphone() as source:
                print("Jarvis Active")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)   
                command = r.recognize_google(audio)   
                processcommand(command)
           #print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        except Exception as e:
            print("Error; {0}".format(e))
