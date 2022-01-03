from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as tsmg
try:
    import pyttsx3

    g = 'i'
    eng = pyttsx3.init('sapi5')
    voices = eng.getProperty('voices')



    def speak(audio, voi):
        eng.setProperty('voice', voices[voi].id)
        eng.say(audio)
        eng.runAndWait()

    root = Tk()
    def choose():
        global g
        filename = filedialog.askopenfilename(title='Choose a file')
        filename = filename.replace("/", "//")
        with open(filename) as file:
            content = file.read()
        
        g = content
        tsmg.showinfo("Text to audio", "Sucessfully imported")
        c.pack()
    def say():
        speak(g, 0)

    root.geometry('500x100')
    root.title('Text to Audio')

    b = Button(text='Choose a file', width=500, command=choose)
    c = Button(text='Say the audio', command=say)
    b.pack(pady=10)


    root.mainloop()
except Exception as e:
    print(e)
