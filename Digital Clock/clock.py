from tkinter import *
import time

root = Tk()
root.title("Digital Clock")

def update_clock():
    current_time = time.strftime("%I:%M:%S %p")
    time_text.config(text=current_time)
    time_text.after(1000, update_clock)

time_text = Label(root, font=("calibri", 40, 'bold'), foreground='white', background='black')
time_text.pack(anchor='center')

update_clock()

root.mainloop()