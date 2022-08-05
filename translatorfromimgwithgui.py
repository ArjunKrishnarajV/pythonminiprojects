import pytesseract as tess
from googletrans import Translator
tess.pytesseract.tesseract_cmd = r'C:\Users\HP\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import ImageTk, Image
import PIL.Image
from tkinter import *
import tkinter
from tkinter import filedialog
translator = Translator()
window = tkinter.Tk()
window.iconbitmap('C:/Users/HP/Downloads/logo.ico')
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.title("Translator Python Project")
window.geometry("%dx%d"%(width,height))
x= Label(window,text="Translator",font=("Arial",20))
x.place(relx=0.5,rely=0.1,anchor='center')
select= Label(window,text="Select an image :",font=("Arial",15))
select.place(relx=0.4,rely=0.25,anchor='center')
def selectimg():
     window.filename=filedialog.askopenfilename(initialdir="C:/",title="Select an image",filetypes=(("jpeg files","*.jpg"),("png files","*.png")))
bt=Button(window,text="Go",command=selectimg)
bt.place(relx=0.6,rely= 0.25,anchor='center')
def translate():
          img = PIL.Image.open(window.filename)
          txt = tess.image_to_string(img)
          f=open("output.txt","w");
          f.write(txt);
          out = translator.translate(txt,dest='ta')
          acttext = Label(window, text=txt, font=("Arial", 11))
          acttext.place(relx=0.5, rely=0.5, anchor='center')
          transtext = Label(window,text=out.text,font=("Arial",9))
          transtext.place(relx=0.5,rely=0.7,anchor='center')
trans=Button(window,text ="Translate Now",command=translate)
trans.place(relx=0.5,rely=0.35,anchor='center')
window.mainloop()
