import pyttsx3
import datetime
from tkinter import *
import tkinter
window = tkinter.Tk()
window.iconbitmap('C:/Users/HP/Downloads/imageonline-co-roundcorner (5).ico')
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
frnd = pyttsx3.init()
frnd. setProperty("rate", 170)
voices = frnd.getProperty('voices')
window.title("Text To Speech")
x= Label(window,text="Text 2 Speech",fg='white',bg='blue',font=("Arial",20))
window.geometry("%dx%d"%(width,height))
x.place(relx=0.5,rely=0.3,anchor='center')
txt = Entry(window,width=50)
txt.place(relx=0.5,rely=0.4,anchor='center')
window.configure(bg='blue')
def clicked():
    current = datetime.datetime.now()
    if(gender_hold.get()=="Female"):
        frnd.setProperty('voice', voices[1].id)
        filename = "SpeechOutFemale" + str(current.hour) + str(current.minute) + str(current.second) + ".mp3"
    if (gender_hold.get() == "Male"):
        frnd.setProperty('voice', voices[0].id)
        filename = "SpeechOutMale" + str(current.hour) + str(current.minute) + str(current.second) + ".mp3"
    text = txt.get()
    frnd.say(text)
    frnd.save_to_file(text,filename)
    frnd.runAndWait()
maleorfemale = {"Male","Female"}
z= Label(window,text="A Project by Apoorva and Team BTech IT SREC",fg='white',bg='black',font=("Arial",8))
z.place(relx=0.98,rely=0.98,anchor='se')
gender_hold = tkinter.StringVar(window)
gender_hold.set("Male")
gender = tkinter.OptionMenu(window,gender_hold,*maleorfemale)
gender.place(relx=0.41,rely= 0.5,anchor='center')
bt= Button(window,text="Go",command=clicked)
bt.place(relx=0.6,rely=0.5,anchor='center')
window.mainloop()
