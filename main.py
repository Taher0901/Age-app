from tkinter import *
from tkinter import messagebox

#1 This is the root of the application (The main window)
app = Tk()
app.geometry("400x200")
app.config(background="yellow")

#2 App Title 
app.title("Age Calculator")

#3 Label() is a funcion to write something in the application. Label(main window, text to be written)
text_label = Label(app, text="Enter Your Age",height=1,font=("Arial", 20),relief="groove",borderwidth=0,bg="yellow") 
text_label.pack()## To make the words be printed on the application we use pack() ###

#4 The age that the user is going to put
age = StringVar() ##StringVar() ==> value of age is going to be decided later
age.set("00")## Default value = 0 ##
age_input = Entry(app,width=2,font=("Arial",30), textvariable=age, relief="groove",borderwidth=0,bg="yellow" )## To make the input that user is going to be put we use Entry(main window, input) , textvariable=age means that the input will be saved to the variable age ##
age_input.pack()## To make the words be printed on the application we use pack() ###

#5 Function that calculates the age in months and weeks
def calc():
    agecalc = age.get()## agecalc equals the value of age ( we use get() )
    if len(agecalc) <= 2: 
        messagebox.showinfo("You Age In All Time Units", f"Your age in months is: {int(agecalc) * 12}\nYour age in weeks is: {int(agecalc) * 52}")## Opens a new window by function messagebox() and showinfo() to print the title and the text  
    else:
        messagebox.showinfo("How old are you?!?!?!?","You can't write more than 2 numbers!")

#6 Function To backspace        
def delete():
    age_input.delete(0,END)
def backspace():
    age_input.delete(len(age_input.get())-1,END) 

#7 Button() to call funcion. Button(main window, text inside the button, command is the function done when pressing the button)  
btn1 = Button(app,text="Calculate Age",bg="yellow",command=calc)## To make the words be printed on the application we use pack() ###
btn1.pack(side="left")
btn2 = Button(app,text="Delete",bg="yellow",command=delete)
btn2.pack(side="right")
btn3 = Button(app,text="Backspace",bg="yellow",command=backspace)
btn3.pack(side="right")
app.mainloop()