from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Aaryanathan's Digital Clock")
label = Label(root, font=("Sans", 80), background="black", foreground="cyan")
label.pack(anchor = "center")

def clock():
    time = strftime("%H:%M:%S %p")
    label.config(text=time)
    label.after(1000, clock)
clock()

mainloop()