from tkinter import *

window = Tk()
window.title("My First GUI Pfrogram")
window.minsize(width=500, height=300)

#label

my_label = Label(text="I am a Label",font=("Ariel", 24,"italic"))
my_label.pack(side="left")

my_label["text"] = "New Text"
my_label.config(text="New Text")


button = Button(text="Click Me")


window.mainloop()