#Online Class
import win10toast
import pyttsx3
import os
import webbrowser
import time
# Setting up voice
eng = pyttsx3.init('sapi5')
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[0].id)

def speak(audio):
    
    eng.say(audio)
    eng.runAndWait()
def online_classes():
    speak("Seting up your device for online classes")
    webbrowser.open_new_tab('https://meet.google.com')
    time.sleep(15)
    webbrowser.open_new_tab('https://web.whatsapp.com')
    time.sleep(5)
    notificate = win10toast.ToastNotifier()
    notificate.show_toast('Setup done!', ' ', duration=5)
    exit()

online_classes()
