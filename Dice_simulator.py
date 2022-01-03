import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


print("Recognizing...")    
query = recognize(audio, language='en-in') #Using google for voice recognition.
print(f"User said: {query}\n")  #User query will be printed.
# print(e)    
print("Say that again please...")   #Say that again will be printed in case of improper voice 

print(query)

takeCommand()

 