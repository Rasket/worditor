from tkinter import *
from tkinter import messagebox
import random 
from tkinter.filedialog import askopenfilename
import curses
import os
import asyncio
from playsound import playsound


def play_button_sound():
	#playsound('soundbutton.mp3', False) second argument not work on linux



def open_text():
	play_button_sound()
	filename = askopenfilename()
	print(filename)
	with open(filename) as f:
		text.insert('1.0', f.read())
	

 
def save_text():
	name = 'save' + str(random.randint(-1000,1000)) + '.txt'
	with open(str(name), 'w+') as file:
		file.write(text.get(1.0, END))
		messagebox.showinfo("GUI Python", 'Your file saved as ' + name)
	
 
 
def delete_text():
	text.delete(1.0, END)
	    
 
 
root = Tk()


root.title("Some boring title")
root.geometry("800x600")


text = Text(width=500, height=30)
text.pack()
 
frame = Frame()
frame.pack()
Button(frame, text="Save text",
       command=save_text, height = 400, width  = 28).pack(side=LEFT)
Button(frame, text="Open text",
       command=open_text, height = 400, width  = 28).pack(side=LEFT)
Button(frame, text="Delete text",
       command=delete_text, height = 400, width  = 28).pack(side=LEFT) 
label = Label()
label.pack()
root.mainloop()







