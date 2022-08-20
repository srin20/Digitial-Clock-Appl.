from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title("CLOCK")
def time():
    string=strftime('%H:%M:%S')
    Label.config(text=string)
    Label.after(1000,time)
Label=Label(root, font=("DS-Digital",100),background='yellow')
Label.pack(anchor='center')
time()
mainloop()