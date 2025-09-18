from tkinter import *
import time
from tkinter import messagebox

root = Tk()
root.title("Countdown Timer")
root.geometry('300x250')

def submit():
    try: 
        time_sec = (int(hours.get()) * 3600) + (int(mins.get()) * 60) + int(secs.get())

    except:
        print("Please input the right value.")
    
    while time_sec > -1:
        minutes, seconds = divmod(time_sec, 60)
        hour = 0
        if minutes > 60:
            hour, minutes = divmod(minutes, 60)

        hours.set("{0:2d}".format(hour))
        mins.set("{0:2d}".format(minutes))
        secs.set("{0:2d}".format(seconds))

        root.update()
        time.sleep(1)

        if time_sec == 0:
            messagebox.showinfo("Countdown Timer", "Time's up ")
            hours.set("00")
            mins.set("00")
            secs.set("00")

        time_sec -= 1


hours = StringVar()
mins = StringVar()
secs = StringVar()

hours.set("00")
mins.set("00")
secs.set("00")

hourEntry = Entry(root, width=3, textvariable=hours, font=("Arial",18,""))
hourEntry.place(x=80, y=20)

minEntry = Entry(root, width=3, textvariable=mins, font=("Arial",18,""))
minEntry.place(x=120, y=20)

secEntry = Entry(root, width=3, textvariable=secs, font=("Arial",18,""))
secEntry.place(x=160, y=20)

btn = Button(root, text="Set the Timer", bd=5, command=submit)
btn.place(x = 95,y = 70)

label = Label(root, text='Created by Abdullah with GeekForGreek\'s guidence.')
label.place(x = 17,y = 120)
root.mainloop()