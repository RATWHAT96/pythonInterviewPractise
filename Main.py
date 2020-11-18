#!/usr/local/bin/python3

import random
import tkinter as tk
import time

""" Variables and Data Structures """

motivational = { 1:"Why this company?", 2:"Why this role?", 3:"Why do you want to work in this industry?", 
                 4:"Why do you want be software developer?"}

competency = { 1:"Describe a time when you exhibited good teamwork", 2:"Provide an example of when you encountered problems in a team", 3:"Describe a time when you have been able to demonstrate flexibility?", 4:"What is my greatest weakness?", 5:"What is your biggest achievement?", 6:"Explain an instance when you influenced someone", 7:"Which skills did you gain during your internship or past investment banking experience that will make you a good fit for this role?", 8:"What motivates you?", 9:"What three things would your friends say about you?", 
                10:"Speak about a time you had to deal with rejection.", 11:"Provide an example of when you encountered problems as an individual and how you dealt with it?", 12:"Explain a time you had a difficult situation and what you did to overcome it", 13:"Can you talk about your experience of changing your approach quickly to achieve a goal?", 14:"Tell me about a time when you failed to meet an objective", 15:"What would you do if you were unable to meet a deadline?", 16:"Describe a time that you faced multiple competing deadlines – Which did you prioritize?", 17:"Provide an example of a time when you assessed a problem and understood its root causes. How did you analyze the information?", 
                18:"You're taking a document to an important meeting that starts in a few minutes and you find a prominent typo. Time is running short and you can’t reprint the document. What would you do?", 19:"Describe a situation in which you changed something", 20:"What's a time you saw something wrong in a team/project/activity you were doing?", 21:"Tell me about a situation where you showed leadership", 22:"Describe a time when you successfully persuaded a group of people or a team to agree with you", 23:"Describe a time when you had to give a presentation to a group of people", 24:"How do you adapt your presentation style to meet the needs of an audience?", 25:"Describe a time when you used your negotiation skills", 
                26:"Name a time you convinced someone to do something"}

t = 0

""" Functions """
def countdown():
    global t
    if t>0:
        timer.config(text=t)
        t=t-1
        timer.after(1000,countdown)
    else:
        timer.config(text="times up!!!")

def next1():
    global t
    t = 0
    timer.after(1000, reset)
    timer.config(text="Next Question")
    timer.after(1000, motivation)

def next2():
    global t
    t = 0
    timer.after(1000, reset)
    timer.config(text="Next Question")
    timer.after(1000, compet)

def motivation():
    qstn.config(text=motivational.get(random.randint(1,4)))
    countdown()

def compet():
    qstn.config(text= competency.get(random.randint(1,26)))
    countdown()

def reset():
    global t 
    t = 120

""" GUI """
# essentially the html of the gui, add any visual elements to the root
root = tk.Tk()

root.title("Interview Practise")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# create a canvas and specify that it should be attached to the root window and customise the canvas
canvas = tk.Canvas(root, height = 900, width = 1348, bg="black")
canvas.pack() #this attaches it to the root

# add a frame (basically a div) to the root 
frame = tk.Frame(root)
frame.place(relwidth = 1, relheight = 1) #adjust position and size of frame

background_image = tk.PhotoImage(file = 'jobInterviewPNG.png')
background_label = tk.Label(frame, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

# add label to contain question
qstn = tk.Label(frame, text = "..........................", padx = 10, pady=2, fg = 'black', bg='#719646', wraplength= 300, justify = 'center')
qstn.place(relx = 0.25, rely = 0.09, relwidth = 0.25, relheight = 0.3)

# adding a button to the frame
motButton = tk.Button(frame, text = "Motivation", padx = 10, pady=2, fg = 'black', bg='white', command = next1, borderwidth = 0)
motButton.place(relx = 0.8, rely = 0.23, relwidth = 0.1, relheight = 0.1)

compButton = tk.Button(frame, text = "Competency", padx = 10, pady=2, fg = 'black', bg='#719646', command = next2)
compButton.place(relx = 0.6, rely = 0.23, relwidth = 0.1, relheight = 0.1)

timer = tk.Label(frame, text = "Timer",  justify='center', bg ='#719646')
timer.config(font=("Courier", 16))
timer.place(relx = 0.7, rely = 0.08, relwidth = 0.1, relheight = 0.1)

# open gui window 
root.mainloop()
