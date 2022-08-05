from tkinter import *
import webbrowser
import tkinter
window = tkinter.Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.title("Google Chrome")
x= Label(window,text="   Google",font=("Arial",35))
window.geometry("%dx%d"%(width,height))
x.place(relx=0.5,rely=0.3,anchor='center')
txt = Entry(window,width=30)
txt.place(relx=0.5,rely=0.4,anchor='center')
def clicked():
    link ="https://google.com/search?q="+txt.get()
    webbrowser.open(link)
bt= Button(window,text="Go",command=clicked)
bt.place(relx=0.6,rely=0.4,anchor='center')
window.mainloop()
