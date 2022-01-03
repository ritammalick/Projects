import pyautogui
import time
time.sleep(10)
pyautogui.write('''import game
import pyautogui

# Setting up voice
eng = pyttsx3.init('sapi5')
voices = eng.getProperty('voices')

with open('D:\\My projects\\Vs code\\Python\\Projects\\AI - Ritam Mallick\\voice') as f:
    voi = f.read()

with open('D:\\My projects\\Vs code\\Python\\Projects\\AI - Ritam Mallick\\user_name') as u:
    name = u.read()
with open('D:\\My projects\\Vs code\\Python\\Projects\\AI - Ritam Mallick\\ai') as a:
    ai_name = a.read()

v = int(voi)

print()
eng.setProperty('voice', voices[v].id)

# Functions
def notification(title, body, duration):
    notificate = win10toast.ToastNotifier()
    notificate.show_toast(title, body, duration=duration)
def wait(seconds):
    time.sleep(seconds)

def speak(audio):
    
    eng.say(audio)
    eng.runAndWait()

def wishMe():
    webbrowser.Chrome()

    speak(f'Hi {name}, I am your virtual assistant {ai_name}')
    print(f"AI: Hi {name}, I am your virtual assistant {ai_name}")
    time.sleep(0.5)

    speak(f"type 'help' to see what can i do ")
    print(f"{ai_name}: type 'help' to see what can i do ")   

def restart():
    speak('Restarting')  

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        question= r.recognize_google(audio, language='en-in')
        print(f"User said: {question}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return question


    

# Main


        elif 'settings'in question:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Settings")
        elif 'edge'in question:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge")
        
        elif 'cloud'in question:
            os.startfile("C:\\Program Files\Adobe\\Adobe Creative Cloud\ACC\\Creative Cloud.exe")
        elif 'notepad'in question:
            speak("opening notepad")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.exe')
        elif 'paint'in question:
            speak('opening paint')
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint")
        elif 'worpad'in question:
            speak("opening wordpad")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\WordPad")
        elif 'manager'in question:
            speak("opening task manager")
            os.startfile('C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.exe')
        
        

        
        elif question=="what is your name":
            speak(ai_name)
            print(ai_name)
        elif 'my'in question and 'name is' in question:
            g = question.split(" name is ")
            with open('D:\\My projects\\Vs code\\Python\Projects\\AI - Ritam Mallick\\Dictionary.py'):
                print()


        elif 'time' in question:
            print(datetime.datetime.now)

        elif 'date' in question:
            from datetime import date

            pp = date.today()
            d2 = pp.strftime("%B %d, %Y")
            print(d2)
            

        

        elif 'game' in question:
            speak("Which game do you want to play? 1., The Perfect guess, 2., Rock Paper Scissor\n")
            ask = input("Which game do you want to play?\n 1. The Perfect guess\n 2. Rock Paper Scissor\n")
            ask.lower()
            if '1' in ask:
                game.perfect_guess()
            else:
                game.rock_paper_scissor()

        elif 'what' in question:
            
            c = question.split(" ")
            l = len(c)
            query = c[-1]
            webbrowser.open_new(f'en.wikipedia.org/wiki/{query}')
        elif 'change your name' in question:
            with open('D:\\My projects\\Vs code\\Python\\Projects\\AI - Ritam Mallick\\ai', 'w')as change:
                speak('Enter my new name')
                change.write(str(input("Enter my new name: ")))
                speak('Please restart the program to see the changes')
        elif 'restart' in question:
)''', interval=0.01)



