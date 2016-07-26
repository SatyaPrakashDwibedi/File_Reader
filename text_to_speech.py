from pyttsx import *
from Tkinter import *
from time import sleep
from tkFileDialog import *
import tkMessageBox as msg
root=Tk()
en=init()
a=raw_input("DO YOU WANT TO READ A FILE\nAnswer Y/N\n$$")
if a=='Y':
    open_file=askopenfile(parent=root,mode='rb',title="File To Be Read")
    if open_file !=None:
        content=open_file.read()
        i=content
        en.say(i)
if a=='N':
    i=raw_input("Enter Message To Be Told")
    en.say(i)

rate=en.getProperty('rate')
en.setProperty('rate',rate-50)
en.runAndWait()
msg.showinfo("hey",message="This Is The End Of The File Run Again To Read Another")
root.destroy()
