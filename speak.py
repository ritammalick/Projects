

import pyttsx3
import pyautogui as pg


eng = pyttsx3.init('sapi5')
voices = eng.getProperty('voices')



def speak(audio, voi):
    eng.setProperty('voice', voices[voi].id)
    eng.say(audio)
    eng.runAndWait()
    

speak('Hi, I am Priyam Mallick.', 0)
speak('Hi, I am swapna MAllick, and I am the mother of Pruyam', 1)

exit()