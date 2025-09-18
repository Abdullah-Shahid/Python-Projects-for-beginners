from tkinter import *


root = Tk()
root.title("Tip Calculator")
root.geometry("200x210")


def submit():
    calculate_bill = bill.get() * (1 + (tip.get()/100)) / num_of_split.get()
    final_amount = "{:.2f}".format(calculate_bill, 2)
    ans.set(f"Final Amount: {final_amount}")


bill = DoubleVar()
tip = IntVar()
num_of_split = IntVar()
ans = StringVar()


title = Label(root, text='Tip Calculator', font=("Arial",12,"bold"), foreground='blue').grid(row=0, column=0)

billLabel = Label(root, text='Bill: ', font=("Arial",12,"")).grid(row=2, column=0)
billEntry = Entry(root, textvariable=bill, width=5, font=("Arial",10,"")).grid(row=2, column=1)

tipLabel = Label(root, text='Tip: ', font=("Arial",12,"")).grid(row=3, column=0)
tipEntry = Entry(root, textvariable=tip, width=5, font=("Arial",10,"")).grid(row=3, column=1)

nosLabel = Label(root, text='Number of split: ', font=("Arial",12,"")).grid(row=4, column=0)
num_of_splitEntry = Entry(root, textvariable=num_of_split, width=5, font=("Arial",10,"")).grid(row=4, column=1)


btn = Button(root, text='Calculate', command= submit, foreground='white', background='blue', font=("Arial",12,"")).grid(row=5, column=0)

ans.set(" ")
ansLabel = Label(root, textvariable=ans, font=("Arial", 12, 'bold')).grid(row=7, column=0)



root.mainloop()