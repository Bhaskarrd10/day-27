import tkinter

window = tkinter.Tk()
window.title("My First GUI Pfrogram")
window.minsize(width=500, height=300)

#label

my_label = tkinter.Label(text="I am a Label",font=("Ariel", 24,"italic"))
my_label.pack(side="left")




window.mainloop()