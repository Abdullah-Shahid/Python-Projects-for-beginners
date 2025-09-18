from tkinter import *
import time


root = Tk()
root.title("Age Calculator")
root.geometry("650x300")

def calculate_age():
    user_bd = int(birth_year.get())
    current_year = int(time.strftime("%Y"))
    age = current_year - user_bd
    user_age.set(f"You are {age} years old.")
    


birth_year = StringVar()
user_age = IntVar()


bd_label = Label(root, text="Enter your year of birth:", font=("Arial", 13))
bd_label.place(x= 10, y=10)

bd_entry = Entry(root, textvariable=birth_year,  font=("Arial", 12))
bd_entry.place(x=15, y=40)

bd_btn = Button(root, text="Calculate Age", font=("Arial", 12, 'bold'), foreground="white", background='blue', command=calculate_age)
bd_btn.place(x=15, y=70)

age_label = Label(root, textvariable=str(user_age), font=("Arial", 13, 'bold'), foreground='blue')
age_label.place(x=15, y=110)


root.mainloop()