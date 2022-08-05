from PIL import ImageGrab
import numpy as np
import cv2
import tkinter
import datetime
import webbrowser as wb
from tkinter import *
from win32api import GetSystemMetrics
window = tkinter.Tk()
window.iconbitmap('scrlogo.ico')
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.title("Screen Recorder By Arjun K")
x= Label(window,text="Screen Recorder",fg='white',bg='black',font=("Arial",20))
window.geometry("%dx%d"%(width,height))
x.place(relx=0.5,rely=0.4,anchor='center')
y = Label(window,text="To stop recording go to the recording window and press Q",fg='white',bg='black',font=("Arial",15))
y.place(relx=0.5,rely=0.6,anchor='center')
z= Label(window,text="A Project by Arjun K BE ICE PSG Tech",fg='white',bg='black',font=("Arial",8))
z.place(relx=0.98,rely=0.98,anchor='se')
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
isrecording = False
window.configure(bg='black')
def clicked() :
    current = datetime.datetime.now()
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    filename = "Output" + str(current.hour) + str(current.minute) + str(current.second) + ".mp4"
    capvideo = cv2.VideoWriter(filename,fourcc,20.0,(width,height))
    while True:
       # isrecording = True
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_array = np.array(img)
        finalimg = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        cv2.imshow('Screen Recorder', finalimg)
        capvideo.write(finalimg)
        if cv2.waitKey(10) == ord('q'):
            cv2.destroyAllWindows()
            wb.open(filename)
            #window.destroy()
            break
    return
bt= Button(window,text="Rec",height = 2,width= 6,fg='red',bg='black',command=clicked)
bt.place(relx=0.5,rely=0.5,anchor='center')
window.mainloop()
