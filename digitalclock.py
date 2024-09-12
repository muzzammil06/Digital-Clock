from tkinter import *
from time import *

root = Tk()
root.title("Digital Clock")

def update():
    time_string = strftime('%H:%M:%S %p')
    time_label.config(text=time_string)
    time_label.after(1000,update)
    day_string = strftime('%A')
    date_label.config(text=day_string)

    date_string = strftime("%d %B %Y")
    date_label.config(text=date_string)
    

time_label = Label(root, font=('FreeInk', 50, 'bold'), background='black',foreground='violet')
time_label.pack()

date_label = Label(root,font=("FreeInk",25,"bold"),bg="white")
date_label.pack()

update()

root.mainloop()